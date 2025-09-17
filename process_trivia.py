import json
import os
import random
import re

def get_character_stories(story_dir):
    stories = {}
    all_files = [f for f in os.listdir(story_dir) if f.endswith('.txt')]
    for filename in all_files:
        with open(os.path.join(story_dir, filename), 'r', encoding='utf-8') as f:
            content = f.read()
            # Split file content into character stories
            # A character story starts with the character's name in caps, followed by a colon.
            char_sections = re.split(r'\n([A-Z][a-zA-Z\s\'.]+):\n', content)
            if len(char_sections) > 1:
                # The regex split results in a list like ['', 'CHAR1', 'story1', 'CHAR2', 'story2', ...]
                i = 1
                while i < len(char_sections):
                    char_name = char_sections[i].strip()
                    char_story = char_sections[i+1].strip()
                    stories[char_name] = char_story
                    i += 2
    return stories

def find_explanation(story_text, question, answer):
    if not story_text:
        return "No explanation found."
    sentences = story_text.split('.')
    # Look for sentences containing the answer.
    possible_explanations = [s.strip() + '.' for s in sentences if answer in s]
    if not possible_explanations:
        return "No explanation found."

    # Try to find a sentence that also has some keywords from the question.
    question_keywords = set(question.lower().split())
    for p in possible_explanations:
        if any(keyword in p.lower() for keyword in question_keywords):
            return p

    # If no sentence with keywords is found, return the first sentence with the answer.
    return possible_explanations[0]

def get_wrong_answers(all_answers, correct_answer, character_answers):
    wrong_answers = set()

    # Prioritize answers from the same character
    potential_wrong = [ans for ans in character_answers if ans != correct_answer]
    random.shuffle(potential_wrong)
    for ans in potential_wrong:
        if len(wrong_answers) < 3:
            wrong_answers.add(ans)

    # Fill up with other answers if needed
    if len(wrong_answers) < 3:
        other_answers = [ans for ans in all_answers if ans != correct_answer and ans not in wrong_answers]
        random.shuffle(other_answers)
        for ans in other_answers:
            if len(wrong_answers) < 3:
                wrong_answers.add(ans)

    return list(wrong_answers)

def process_trivia_file(trivia_path, story_dir):
    with open(trivia_path, 'r', encoding='utf-8') as f:
        trivia_data = json.load(f)

    # I'll create a dictionary of stories, where the key is the character name.
    # This is a more robust way to get character stories.
    character_stories = {}
    all_story_files = [f for f in os.listdir(story_dir) if f.endswith('.txt')]
    for filename in all_story_files:
        with open(os.path.join(story_dir, filename), 'r', encoding='utf-8') as f:
            content = f.read()
            # The character stories are separated by "~~Character Name ends here~~"
            # So I will split the content by this delimiter.
            # The character name is at the beginning of each section.

            # Let's find all character names from the trivia file.
            all_chars = sorted(list(set(item['source'] for item in trivia_data)), key=len, reverse=True)

            for char in all_chars:
                # A character's story starts with their name and a colon.
                # It ends with "~~Character Name ends here~~" or similar.
                match = re.search(rf'^{re.escape(char)}:(.*?)(~~{re.escape(char)}.*?ends here~~)', content, re.DOTALL | re.IGNORECASE | re.MULTILINE)
                if match:
                    character_stories[char] = match.group(1).strip()

    all_answers = [item['answer'] for item in trivia_data]

    character_answers = {}
    for item in trivia_data:
        source = item['source']
        if source not in character_answers:
            character_answers[source] = []
        character_answers[source].append(item['answer'])

    new_trivia_data = []
    for item in trivia_data:
        character_name = item['source']
        story_text = character_stories.get(character_name, "")

        explanation = find_explanation(story_text, item['question'], item['answer'])

        new_item = {
            "category": character_name,
            "difficulty": "medium",
            "question": item["question"],
            "correct_answer": item["answer"],
            "wrong_answers": get_wrong_answers(all_answers, item["answer"], character_answers.get(character_name, [])),
            "explanation": explanation,
            "id": item["id"]
        }
        new_trivia_data.append(new_item)

    with open(trivia_path, 'w', encoding='utf-8') as f:
        json.dump(new_trivia_data, f, indent=4)

    print(f"Processed {trivia_path} successfully.")

if __name__ == "__main__":
    process_trivia_file("trivia/genshin_trivia_22.json", "GenshinStories/")
