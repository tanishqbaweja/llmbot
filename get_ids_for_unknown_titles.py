import json

def get_ids_for_unknown_titles():
    """
    Gets the IDs of the questions with "Unknown" anime titles.
    """
    with open("anime_trivia.json", "r") as f:
        data = json.load(f)

    unknown_title_ids = []
    for question in data:
        if question["anime_title"] == "Unknown":
            unknown_title_ids.append(question["id"])

    print(unknown_title_ids)

if __name__ == "__main__":
    get_ids_for_unknown_titles()
