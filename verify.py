import json

def verify_trivia_file():
    try:
        with open('trivia_questions.json', 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return
    except FileNotFoundError:
        print("Error: trivia_questions.json not found.")
        return

    # 1. Check total number of questions
    if len(data) != 2000:
        print(f"Error: Expected 2000 questions, but found {len(data)}.")
        return

    required_keys = ["ID", "category", "difficulty", "question_text", "correct_answer", "wrong_answers", "explanation"]
    errors = []

    for i, question in enumerate(data):
        # 2. Check for required fields
        missing_keys = [key for key in required_keys if key not in question]
        if missing_keys:
            errors.append(f"Question {i+1} (ID: {question.get('ID', 'N/A')}) is missing keys: {', '.join(missing_keys)}")
            continue # Skip further checks for this question

        # 3. Check that explanation is not empty
        if not question.get("explanation") or not isinstance(question["explanation"], str) or not question["explanation"].strip():
            errors.append(f"Question {i+1} (ID: {question['ID']}) has an empty or invalid explanation.")

    if errors:
        print("Verification failed with the following errors:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Verification successful!")
        print("- Total number of questions: 2000")
        print("- All questions have the required fields.")
        print("- No empty explanations found.")

if __name__ == "__main__":
    verify_trivia_file()
