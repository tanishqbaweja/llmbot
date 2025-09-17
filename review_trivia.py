import json

def review_trivia_file(filepath="genshin_trivia.json"):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            trivia_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file '{filepath}' is not a valid JSON file.")
        return

    total_questions = len(trivia_data)

    character_questions = {}
    for question in trivia_data:
        category = question.get("category")
        if category:
            character_questions.setdefault(category, 0)
            character_questions[category] += 1

    character_count = len(character_questions)

    print("--- Trivia File Review ---")
    print(f"Total number of questions: {total_questions}")
    print(f"Total number of unique characters: {character_count}")

    print("\n--- Question Count per Character ---")
    all_characters_have_10_questions = True
    for character, count in sorted(character_questions.items()):
        print(f"- {character}: {count} questions")
        if count < 10:
            print(f"  *** WARNING: {character} has fewer than 10 questions! ***")
            all_characters_have_10_questions = False

    print("\n--- Verification ---")
    if total_questions > 1000:
        print(f"[SUCCESS] Total questions ({total_questions}) is over 1000.")
    else:
        print(f"[FAILURE] Total questions ({total_questions}) is not over 1000.")

    if all_characters_have_10_questions:
        print("[SUCCESS] All characters have at least 10 questions.")
    else:
        print("[FAILURE] Not all characters have at least 10 questions.")

if __name__ == "__main__":
    review_trivia_file()
