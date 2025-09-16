import json
import os

def create_question(anime_title, category, difficulty, question, correct_answer, wrong_answers, explanation):
    """
    Creates a new trivia question and adds it to the anime_trivia.json file.
    """
    file_path = 'anime_trivia.json'

    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                questions = json.load(f)
            except json.JSONDecodeError:
                questions = []
    else:
        questions = []

    new_id = 1
    if questions:
        new_id = max(q['id'] for q in questions) + 1

    new_question = {
        "category": category,
        "difficulty": difficulty,
        "question": f"In '{anime_title}', {question}",
        "correct_answer": correct_answer,
        "wrong_answers": wrong_answers,
        "explanation": explanation,
        "id": new_id
    }

    questions.append(new_question)

    with open(file_path, 'w') as f:
        json.dump(questions, f, indent=4)

    print(f"Successfully created question with ID {new_id}.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 8:
        print("Usage: python create_question.py \"<anime_title>\" \"<category>\" \"<difficulty>\" \"<question>\" \"<correct_answer>\" \"<wrong_answers>\" \"<explanation>\"")
        sys.exit(1)

    create_question(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6].split(','), sys.argv[7])
