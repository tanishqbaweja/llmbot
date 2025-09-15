import requests
import json

# The API endpoint
url = "https://the-trivia-api.com/api/questions?limit=50"

# The list to hold all the new questions
new_questions = []

# Loop 18 times to get 900 questions
for i in range(18):
    print(f"Fetching batch {i+1}/18...")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        questions = response.json()
        new_questions.extend(questions)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during API request: {e}")
        # Decide how to handle the error, maybe break or continue
        break
    except json.JSONDecodeError:
        print(f"Failed to decode JSON from response.")
        continue

print(f"Fetched a total of {len(new_questions)} new questions.")

# Now, read the existing questions
try:
    with open('trivia_questions.json', 'r', encoding='utf-8') as f:
        existing_questions = json.load(f)
except FileNotFoundError:
    print("trivia_questions.json not found. Starting with an empty list.")
    existing_questions = []
except json.JSONDecodeError:
    print("Error reading trivia_questions.json. It might be corrupted. Starting with an empty list.")
    existing_questions = []

# The new questions have a different format. I need to normalize them before appending.
# Target structure: "ID", "category", "difficulty", "question_text", "correct_answer", "wrong_answers", "explanation"
normalized_new_questions = []
for item in new_questions:
    normalized_item = {
        "ID": item.get('id', ''),
        "category": item.get('category', 'General'),
        "difficulty": item.get('difficulty', 'medium'),
        "question_text": item['question'],
        "correct_answer": item['correctAnswer'],
        "wrong_answers": item.get('incorrectAnswers', []),
        "explanation": "Explanation not found." # Placeholder
    }
    normalized_new_questions.append(normalized_item)


# Combine the existing and new questions
combined_list = existing_questions + normalized_new_questions


# Re-ID everything to be sequential
for i, item in enumerate(combined_list, 1):
    item['ID'] = str(i)

# Write the combined list back to the file
with open('trivia_questions.json', 'w', encoding='utf-8') as f:
    json.dump(combined_list, f, indent=2)

print(f"Successfully updated trivia_questions.json with a total of {len(combined_list)} questions.")
