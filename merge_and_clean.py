import json

def merge_and_clean_files(general_file, india_file, output_file):
    # Read the general questions
    with open(general_file, 'r') as f:
        general_questions = json.load(f)

    # Read the India-specific questions
    with open(india_file, 'r') as f:
        india_questions = json.load(f)

    # Combine the two lists of questions
    all_questions = general_questions + india_questions

    # Remove placeholders and duplicates
    cleaned_questions = []
    seen_questions = set()
    for question in all_questions:
        if question.get('category') != 'Placeholder':
            question_text = question.get('question_text')
            if question_text not in seen_questions:
                cleaned_questions.append(question)
                seen_questions.add(question_text)

    # Re-index the questions
    for i, question in enumerate(cleaned_questions):
        question['ID'] = str(i + 1)

    # Write the cleaned data to the output file
    with open(output_file, 'w') as f:
        json.dump(cleaned_questions, f, indent=2)

    print(f"Successfully merged and cleaned {len(cleaned_questions)} questions into {output_file}")

if __name__ == "__main__":
    merge_and_clean_files('trivia_questions.json', 'india_trivia.json', 'trivia_questions.json')
