import json

# Load both files
with open('trivia_questions.json', 'r', encoding='utf-8') as f:
    try:
        general_data = json.load(f)
    except json.JSONDecodeError:
        print("Error reading trivia_questions.json. It might be corrupted.")
        general_data = []

with open('india_trivia.json', 'r', encoding='utf-8') as f:
    try:
        india_data = json.load(f)
    except json.JSONDecodeError:
        print("Error reading india_trivia.json. It might be corrupted.")
        india_data = []

# The structure of the general questions from the API is different.
# Let's normalize it to the target structure.
# Target structure: "ID", "category", "difficulty", "question_text", "correct_answer", "wrong_answers", "explanation"
normalized_general_questions = []
for item in general_data:
    # skip india questions that might be in the general file
    if item.get('ID', ''):
        if item.get('ID', '').startswith('IND'):
            continue

    if 'question' in item and 'correctAnswer' in item:
        normalized_item = {
            "ID": item.get('id', ''),
            "category": item.get('category', 'General'),
            "difficulty": item.get('difficulty', 'medium'),
            "question_text": item['question'],
            "correct_answer": item['correctAnswer'],
            "wrong_answers": item.get('incorrectAnswers', []),
            "explanation": item.get('explanation', 'Explanation not found.')
        }
        if normalized_item['explanation'] != 'Explanation not found.':
            normalized_general_questions.append(normalized_item)

# The india questions are already in the correct format, but might contain placeholders and duplicates.
# Let's clean them.
cleaned_india_questions = []
seen_ids = set()
for item in india_data:
    if 'question_text' in item and not item['question_text'].startswith("Placeholder"):
        if item['ID'] not in seen_ids:
            # fix wrong answers which are not in a list
            if isinstance(item['wrong_answers'], str):
                item['wrong_answers'] = [ans.strip() for ans in item['wrong_answers'].split(',')]
            cleaned_india_questions.append(item)
            seen_ids.add(item['ID'])

# Now combine the two lists
merged_list = normalized_general_questions + cleaned_india_questions

# Re-ID everything to be sequential
for i, item in enumerate(merged_list, 1):
    item['ID'] = str(i)

# Write the merged and cleaned data back to trivia_questions.json
with open('trivia_questions.json', 'w', encoding='utf-8') as f:
    json.dump(merged_list, f, indent=2)

print(f"Successfully merged {len(merged_list)} questions into trivia_questions.json")
