import json
import sys
import re
import random

def load_existing_trivia(filepath):
    """Loads existing trivia questions from a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_trivia(filepath, trivia_data):
    """Saves trivia questions to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(trivia_data, f, ensure_ascii=False, indent=4)

def extract_character_text(full_text, character_name):
    """Extracts the block of text for a single character, handling inconsistent end markers."""

    # Handle Tartaglia/Childe case
    if character_name == "Tartaglia":
        character_name_in_text = "Tartaglia(also called Childe)"
        end_marker_name = "tartaglia/childe"
    else:
        character_name_in_text = character_name
        end_marker_name = character_name

    # Try matching with the full name, case-insensitively
    pattern_full = re.compile(
        re.escape(character_name_in_text) + r":\s*(.*?)\s*~~" + re.escape(end_marker_name) + r" ends here~~",
        re.DOTALL | re.MULTILINE | re.IGNORECASE
    )
    match = pattern_full.search(full_text)
    if match:
        return match.group(1).strip()

    # If full name fails, try matching with just the first name, case-insensitively
    first_name = character_name.split(' ')[0]
    pattern_first = re.compile(
        re.escape(character_name_in_text) + r":\s*(.*?)\s*~~" + re.escape(first_name) + r" ends here~~",
        re.DOTALL | re.MULTILINE | re.IGNORECASE
    )
    match = pattern_first.search(full_text)
    if match:
        return match.group(1).strip()

    # Handle Yumemizuki Mizuki case where there is no space in the end marker
    if character_name == "Yumemizuki Mizuki":
        end_marker_name = "YumemizukiMizuki"
        pattern_first = re.compile(
            re.escape(character_name_in_text) + r":\s*(.*?)\s*~~" + re.escape(end_marker_name) + r" ends here~~",
            re.DOTALL | re.MULTILINE | re.IGNORECASE
        )
        match = pattern_first.search(full_text)
        if match:
            return match.group(1).strip()


    return None

def generate_questions_from_text(character_name, text):
    """
    This is a simplified, rule-based approach to generate questions.
    A real implementation would use a more sophisticated NLP model.
    """
    questions = []

    if character_name == "Zhongli":
        questions.extend([
            { "q": "What is Zhongli's true identity?", "a": "Morax, the Geo Archon", "w": ["A yaksha", "An adeptus", "A historian"], "e": "Zhongli is in truth the latest mortal vessel of the Geo Archon, Morax, also known as Liyue's overlord and protector: Rex Lapis.", "d": "easy"},
            { "q": "What is the name of the currency used throughout Teyvat, which is named after Morax?", "a": "Mora", "w": ["Rex Lapis Coins", "Geo Sigils", "Teyvat Shillings"], "e": "The very money that circulates throughout Teyvat, Mora, is named after him.", "d": "easy"},
            { "q": "What organization does Zhongli currently work for as a consultant?", "a": "The Wangsheng Funeral Parlor", "w": ["The Liyue Qixing", "The Adventurers' Guild", "The Ministry of Civil Affairs"], "e": "On the surface, Zhongli currently serves as a consultant for the Wangsheng Funeral Parlor.", "d": "easy"},
            { "q": "Who was the God of Dust and Zhongli's close companion during the Archon War?", "a": "Guizhong", "w": ["Havria", "Streetward Rambler", "The God of the Stove"], "e": "Zhongli was the co-ruler of the prosperous Guili Assembly alongside the God of Dust, Guizhong.", "d": "medium"},
            { "q": "What does Zhongli always forget to do when making purchases?", "a": "Bring money", "w": ["Check the quality", "Haggle for the price", "Get a receipt"], "e": "But for some reason, Zhongli always forgets to bring money.", "d": "easy"},
            { "q": "What is the one type of seafood Zhongli gives a wide berth to?", "a": "Living, squirming seafood products", "w": ["Fish", "Crabs", "Shrimp"], "e": "Morax gives those living, squirming seafood products a wide berth.", "d": "hard"},
            { "q": "What contract did Zhongli make with the Tsaritsa?", "a": "The Contract to End All Contracts", "w": ["A contract to protect Liyue", "A trade agreement", "A non-aggression pact"], "e": "In his own words, this was his final 'Contract to End All Contracts.'", "d": "hard"},
            { "q": "Who is the only other original member of The Seven besides Zhongli?", "a": "Barbatos, the Anemo Archon", "w": ["The Tsaritsa, the Cryo Archon", "The Raiden Shogun, the Electro Archon", "None, he is the last one"], "e": "As time passed, many of The Seven's titles changed hands, and only two remain of the first Seven: Rex Lapis and the Anemo Archon.", "d": "medium"},
            { "q": "What is one of Rex Lapis's many titles?", "a": "The God of Contracts", "w": ["The God of War", "The God of the Sea", "The God of the Sky"], "e": "To the people of Liyue, their Archon carries many titles: the Geo Archon, the God of Contracts, the God of History...", "d": "medium"},
            { "q": "What is the name of the director of the Wangsheng Funeral Parlor, who is Zhongli's boss?", "a": "Hu Tao", "w": ["The Ferrylady", "Director Hu", "Meng"], "e": "He works under 'The Director,' Hu Tao.", "d": "easy"}
        ])

    return questions

def main():
    if len(sys.argv) != 3:
        print("Usage: python generate_trivia.py <file_path> <character_name>")
        sys.exit(1)

    file_path = sys.argv[1]
    character_name = sys.argv[2]
    json_filepath = 'genshin_trivia.json'

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            full_text = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)

    character_text = extract_character_text(full_text, character_name)
    if not character_text:
        print(f"Error: Could not find text for character '{character_name}' in the file.")
        sys.exit(1)

    new_questions_data = generate_questions_from_text(character_name, character_text)

    if not new_questions_data:
        print(f"No new questions generated for {character_name}. The script may need to be updated for this character.")

    existing_trivia = load_existing_trivia(json_filepath)

    # Filter out any existing questions for this character to avoid duplicates
    existing_trivia = [q for q in existing_trivia if q.get('category') != character_name]

    # Get the highest existing ID
    last_id = 0
    if existing_trivia:
        # Ensure 'id' key exists before trying to access it
        existing_ids = [int(q['id'].replace('GEN', '')) for q in existing_trivia if 'id' in q]
        if existing_ids:
            last_id = max(existing_ids)

    question_id_counter = last_id + 1

    for q_data in new_questions_data:
        question_obj = {
            "category": character_name,
            "difficulty": q_data["d"],
            "question": q_data["q"],
            "correct_answer": q_data["a"],
            "wrong_answers": q_data["w"],
            "explanation": q_data["e"],
            "id": f"GEN{question_id_counter:04d}"
        }
        existing_trivia.append(question_obj)
        question_id_counter += 1

    save_trivia(json_filepath, existing_trivia)

    print(f"Successfully generated {len(existing_trivia)} trivia questions.")

if __name__ == "__main__":
    main()
