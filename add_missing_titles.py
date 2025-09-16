import json

def add_missing_titles():
    """
    Helps to manually add missing anime titles to the anime_trivia.json file.
    """
    with open("anime_trivia.json", "r") as f:
        data = json.load(f)

    for question in data:
        if question["anime_title"] == "Unknown":
            print(f"Question: {question['question']}")
            title = input("Enter the anime title for this question: ")
            question["anime_title"] = title

    with open("anime_trivia.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Successfully updated the anime_trivia.json file with the missing titles.")

if __name__ == "__main__":
    add_missing_titles()
