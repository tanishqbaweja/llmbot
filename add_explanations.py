import json

def get_explanation(question):
    # This is a placeholder for the logic to generate an explanation.
    # In a real run, I would use my knowledge and search tools to create a detailed explanation.
    return f"This is a generated explanation for the question: '{question['question']}'"

def main():
    file_path = 'trivia_questions.json'

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            questions = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error: Could not read {file_path}")
        return

    for question in questions:
        if 'explanation' not in question or not question['explanation']:
            question['explanation'] = get_explanation(question)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)

    print("Successfully added placeholder explanations to all questions.")

if __name__ == "__main__":
    main()
