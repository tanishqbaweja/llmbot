import json

def merge_trivia_files():
    try:
        with open('trivia_questions.json', 'r', encoding='utf-8') as f:
            # Load the existing data, which is a list of objects
            # We need to remove the closing ']' to append new data
            content = f.read()
            if content.strip().endswith(']'):
                content = content.strip()[:-1]

    except FileNotFoundError:
        print("Error: trivia_questions.json not found.")
        return
    except json.JSONDecodeError:
        # If the file is empty or corrupted, start fresh
        content = '['

    # Start writing the output, beginning with the existing content
    with open('trivia_questions.json', 'w', encoding='utf-8') as f:
        f.write(content)

        # If the file was not empty, we need a comma before the new data
        if content.strip() != '[':
            f.write(',\n')

        current_id = 525

        for i in range(1, 11):
            batch_filename = f'batch{i}.json'
            try:
                with open(batch_filename, 'r', encoding='utf-8') as batch_file:
                    batch_data = json.load(batch_file)

                    for question in batch_data:
                        new_question = {
                            "ID": str(current_id),
                            "category": question.get("category", "general_knowledge").replace(" ", "_").lower(),
                            "difficulty": question.get("difficulty", "medium"),
                            "question_text": question.get("question", {}).get("text", ""),
                            "correct_answer": question.get("correctAnswer", ""),
                            "wrong_answers": question.get("incorrectAnswers", []),
                            "explanation": ""
                        }

                        # Write each new question object
                        json.dump(new_question, f, indent=2)
                        f.write(',\n') # Add comma after each object

                        current_id += 1
            except FileNotFoundError:
                print(f"Warning: {batch_filename} not found.")
            except json.JSONDecodeError:
                print(f"Warning: Could not decode JSON from {batch_filename}.")

        # After all batches, we need to remove the last comma and close the list
        f.seek(f.tell() - 2) # Go back to before the last ',\n'
        f.truncate()
        f.write('\n]\n')

    print(f"Successfully merged all batch files. Final question count should be {current_id - 1}.")

if __name__ == "__main__":
    merge_trivia_files()
