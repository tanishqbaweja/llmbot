import json
import re

def get_anime_title_from_question(question):
    """
    Extracts the anime title from the question text.
    This is a helper function that uses regex to find the anime title in the question.
    It looks for text between double quotes.
    """
    match = re.search(r'\"(.+?)\"', question)
    if match:
        return match.group(1)
    return "Unknown"

def clean_data():
    """
    Cleans the anime_trivia.json file.
    """
    with open("anime_trivia.json", "r") as f:
        data = json.load(f)

    for question in data:
        # Add anime_title if it's missing
        if "anime_title" not in question:
            question["anime_title"] = get_anime_title_from_question(question["question"])

        # Clean up wrong_answers format
        if isinstance(question["wrong_answers"], list) and len(question["wrong_answers"]) > 0 and isinstance(question["wrong_answers"][0], str):
            cleaned_answers = []
            for answer in question["wrong_answers"]:
                # Remove extra quotes and brackets
                cleaned_answer = answer.replace("['", "").replace("']", "").replace("'", "")
                cleaned_answers.append(cleaned_answer)
            question["wrong_answers"] = cleaned_answers


        # Standardize category
        question["category"] = "Anime"

        # Standardize difficulty
        question["difficulty"] = question["difficulty"].lower()

    with open("anime_trivia.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Successfully cleaned the anime_trivia.json file.")

if __name__ == "__main__":
    clean_data()
