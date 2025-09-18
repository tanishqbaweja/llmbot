import json
import os
import re
import random
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Use the clean, extracted data as input.
INPUT_JSON_PATH = "trivia/genshin.json"
OUTPUT_JSON_PATH = "trivia/genshin_trivia_22.json" # The final output will overwrite the original file.
STORIES_DIR = "GenshinStories"

def clean_text(text):
    """Removes unwanted characters and whitespace from a string."""
    if not isinstance(text, str):
        return text
    text = text.replace('\\u00a0', ' ').replace('\\n', ' ')
    text = text.replace(u'\u00a0', ' ').replace('\n', ' ')
    text = text.replace('\\"', '"').replace("\\'", "'")
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def normalize_name(name):
    """Normalizes character names for matching."""
    if not isinstance(name, str):
        return ""
    name = name.lower()
    # For names like "Tartaglia(also called Childe)", extract the primary name
    match = re.match(r'([^(]+)', name)
    if match:
        name = match.group(1).strip()
    return name

def load_stories():
    """Loads all character stories from the .txt files."""
    stories = {}
    if not os.path.exists(STORIES_DIR):
        logging.error(f"Stories directory '{STORIES_DIR}' not found.")
        return {}

    logging.info(f"Loading stories from {STORIES_DIR}...")

    for filename in sorted(os.listdir(STORIES_DIR)):
        if filename.endswith(".txt"):
            filepath = os.path.join(STORIES_DIR, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Get character name from the first line, before the colon
                    first_line = content.split('\n', 1)[0]
                    match = re.match(r'^([^:]+):', first_line)
                    if match:
                        char_name = match.group(1).strip()
                        normalized_char_name = normalize_name(char_name)
                        stories[normalized_char_name] = content
                        logging.info(f"Loaded story for '{normalized_char_name}' from file '{filename}'.")
                    else:
                        logging.warning(f"Could not extract character name from first line of '{filename}'.")
            except Exception as e:
                logging.error(f"Error processing file {filename}: {e}")
    return stories

def find_explanation(story_text, answer):
    """Finds a sentence in the story that can serve as an explanation."""
    sentences = re.split(r'(?<=[.!?])\s+', story_text)
    for sentence in sentences:
        if re.search(r'\b' + re.escape(answer) + r'\b', sentence, re.IGNORECASE):
            return clean_text(sentence)
    return None

def generate_wrong_answers(story_text, correct_answer, question):
    """Generates a list of 3 plausible wrong answers from the story text."""
    # This regex looks for capitalized words (proper nouns), capturing up to 3-word phrases.
    potential_answers = re.findall(r'\b[A-Z][a-zA-Z\']+(?:\s[A-Z][a-zA-Z\']+){0,2}\b', story_text)

    wrong_answers = set()
    correct_lower = correct_answer.lower()
    question_lower = question.lower()

    # Expanded list of common words to filter out.
    stopwords = ["the", "a", "an", "it", "is", "was", "were", "he", "she", "they", "what", "when", "where", "why", "how", "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "him", "his", "himself", "her", "hers", "herself", "its", "itself", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "said"]

    for ans in potential_answers:
        ans_cleaned = clean_text(ans)
        ans_lower = ans_cleaned.lower()

        # Filters: avoid short answers, the correct answer, parts of the question, or substrings of the correct answer.
        if len(ans_cleaned) < 3:
            continue
        if ans_lower == correct_lower:
            continue
        if ans_lower in question_lower:
            continue
        if ans_lower in correct_lower or correct_lower in ans_lower:
            continue
        # Filter out common English words that might be capitalized at a sentence's start.
        if " " not in ans_cleaned and ans_lower in stopwords:
             continue

        wrong_answers.add(ans_cleaned)

    # If we still don't have enough, use a fallback to find any other capitalized word.
    if len(wrong_answers) < 3:
        fallback_answers = re.findall(r'\b[A-Z][a-zA-Z\']+\b', story_text)
        for ans in fallback_answers:
            ans_cleaned = clean_text(ans)
            ans_lower = ans_cleaned.lower()
            if len(ans_cleaned) > 3 and ans_lower != correct_lower and ans_lower not in question_lower and ans_lower not in stopwords:
                wrong_answers.add(ans_cleaned)
            if len(wrong_answers) >= 3:
                break

    final_answers = list(wrong_answers)

    # Return a random sample of 3 if available.
    if len(final_answers) >= 3:
        return random.sample(final_answers, 3)
    else:
        # As a last resort, use neutral placeholders if not enough context-aware answers could be found.
        placeholders = ["A different choice", "Another option", "Not this one", "Something else entirely"]
        while len(final_answers) < 3:
            placeholder = random.choice(placeholders)
            if placeholder not in final_answers and placeholder.lower() != correct_lower:
                final_answers.append(placeholder)
        return final_answers

def create_new_question(story_text, character_name):
    """Creates a new, grammatically sound fill-in-the-blank question."""

    # Filter for sentences that are more likely to be good facts.
    potential_sentences = []
    # Reject sentences starting with common conjunctions or pronouns.
    sentence_blacklist = r'^(and|but|so|yet|for|or|nor|while|however|moreover|besides|also|thus|then|if|when|who|what|where|that|which|he|she|it|they)\s'

    # Split by sentence-ending punctuation.
    sentences = re.split(r'(?<=[.!?])\s+', story_text)

    for s in sentences:
        s_cleaned = clean_text(s)
        # Check length, presence of character name, and that it doesn't start with a blacklisted word.
        if 8 < len(s_cleaned.split()) < 40 and character_name.lower() in s_cleaned.lower() and not re.match(sentence_blacklist, s_cleaned, re.IGNORECASE):
            potential_sentences.append(s_cleaned)

    if not potential_sentences:
        return None

    # Try a few times to find a good sentence and answer combo.
    for _ in range(5): # Try up to 5 random sentences
        fact_sentence = random.choice(potential_sentences)

        # Find all potential answers (proper nouns) in the sentence.
        nouns = re.findall(r'\b[A-Z][a-zA-Z\']+(?:\s[A-Z][a-zA-Z\']+){0,2}\b', fact_sentence)
        valid_answers = []
        for noun in nouns:
            noun_lower = noun.lower()
            # Filter out the character's name, short words, or substrings.
            if character_name.lower() not in noun_lower and noun_lower not in character_name.lower() and len(noun) > 3:
                valid_answers.append(noun)

        if not valid_answers:
            continue # Try another sentence

        answer_candidate = random.choice(valid_answers)

        # Final check to ensure the question is not just the character's name and a blank.
        question_text_base = fact_sentence.replace(answer_candidate, "_____")
        if character_name in question_text_base:
            question_text = f"In {character_name}'s story, what fills in the blank: \"{question_text_base}\"?"

            logging.info(f"For new question for '{character_name}', generating wrong answers from story text starting with: {story_text[:200]}")
            return {
                "question": question_text,
                "correct_answer": answer_candidate,
                "wrong_answers": generate_wrong_answers(story_text, answer_candidate, question_text),
                "explanation": fact_sentence
            }

    return None # Return None if no suitable question could be generated after several tries.

def main():
    try:
        with open(INPUT_JSON_PATH, 'r', encoding='utf-8') as f:
            trivia_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"FATAL: Error loading the cleaned data from '{INPUT_JSON_PATH}': {e}")
        return

    print("Loading stories...")
    stories = load_stories()
    if not stories:
        print("FATAL: No stories loaded.")
        return

    print(f"Successfully loaded stories for {len(stories)} characters.")

    new_trivia_list = []
    id_counter = 2001

    processed_characters = set()

    for item in trivia_data:
        character_name = item.get("category")
        if not character_name: continue

        normalized_char_name = normalize_name(character_name)
        processed_characters.add(normalized_char_name)
        story_text = stories.get(normalized_char_name)

        if not story_text:
            print(f"DEBUG: No story found for '{character_name}' (normalized: '{normalized_char_name}'). Skipping.")
            continue

        question_text = clean_text(item.get("question", ""))
        correct_answer_text = clean_text(item.get("correct_answer", ""))

        explanation = find_explanation(story_text, correct_answer_text)

        # If the explanation is invalid or doesn't contain the answer, generate a new question.
        if not explanation or not re.search(r'\b' + re.escape(correct_answer_text) + r'\b', explanation, re.IGNORECASE):
            new_q_data = create_new_question(story_text, character_name)
            if not new_q_data:
                logging.warning(f"Could not generate a new question for {character_name}. Skipping this trivia item.")
                continue
            item_data = new_q_data
        else:
            logging.info(f"For character '{character_name}', generating wrong answers from story text starting with: {story_text[:200]}")
            item_data = {
                "question": question_text,
                "correct_answer": correct_answer_text,
                "wrong_answers": generate_wrong_answers(story_text, correct_answer_text, question_text),
                "explanation": explanation
            }

        new_item = {
            "category": character_name,
            "difficulty": random.choice(["easy", "medium", "hard"]),
            "question": item_data["question"],
            "correct_answer": item_data["correct_answer"],
            "wrong_answers": item_data["wrong_answers"],
            "explanation": item_data["explanation"],
            "id": f"GEN2-{id_counter}"
        }

        # Ensure there are always 3 wrong answers.
        while len(new_item["wrong_answers"]) < 3:
            new_item["wrong_answers"].append(f"Placeholder {len(new_item['wrong_answers'])}")

        new_trivia_list.append(new_item)
        id_counter += 1

    # Add new questions for characters who had stories but no trivia questions
    story_characters = set(stories.keys())
    unprocessed_chars = story_characters - processed_characters
    print(f"Found {len(unprocessed_chars)} characters with stories but no trivia. Generating new questions...")
    for char_norm in unprocessed_chars:
        # Find the original character name to use in the question
        original_char_name = ""
        # A bit of a hack to get the original casing back
        for filename in os.listdir(STORIES_DIR):
             if filename.endswith('.txt'):
                 with open(os.path.join(STORIES_DIR, filename), 'r', encoding='utf-8') as f:
                    first_line = f.readline()
                    match = re.match(r'^([^:]+):', first_line)
                    if match and normalize_name(match.group(1).strip()) == char_norm:
                        original_char_name = match.group(1).strip()
                        break
             if original_char_name: break

        if not original_char_name:
            original_char_name = char_norm.title() # Fallback

        story_text = stories[char_norm]
        for _ in range(15): # Generate up to 15 new questions per character
            new_q_data = create_new_question(story_text, original_char_name)
            if new_q_data:
                new_item = {
                    "category": original_char_name,
                    "difficulty": random.choice(["easy", "medium", "hard"]),
                    "question": new_q_data["question"],
                    "correct_answer": new_q_data["correct_answer"],
                    "wrong_answers": new_q_data["wrong_answers"],
                    "explanation": new_q_data["explanation"],
                    "id": f"GEN2-{id_counter}"
                }
                new_trivia_list.append(new_item)
                id_counter += 1


    with open(OUTPUT_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(new_trivia_list, f, indent=4, ensure_ascii=False)

    print(f"Processing complete. Final trivia file saved to '{OUTPUT_JSON_PATH}' with {len(new_trivia_list)} entries.")
    if os.path.exists(INPUT_JSON_PATH) and INPUT_JSON_PATH == "trivia/extracted_data.json":
        try:
            os.remove(INPUT_JSON_PATH)
            print(f"Removed temporary file: {INPUT_JSON_PATH}")
        except OSError as e:
            print(f"Error removing temporary file {INPUT_JSON_PATH}: {e}")


if __name__ == "__main__":
    main()
