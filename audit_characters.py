import os
import re

def audit_characters():
    """
    Scans all .txt files in the GenshinStories_txt directory
    and prints a unique, sorted list of all character names found.
    """
    directory = "GenshinStories_txt/"
    all_characters = set()

    EXCLUSION_LIST = {
        "summary", "character stories", "character details", "vision", "gnosis",
        "altered character stories", "the fascinating bracelet and the whitesilk mantle",
        "a home-and-away handbook of practical wisdom for the undead",
        "researcher's first magnifying glass", "old duster", "martial arts tournament champion's medal",
        "longevity lock", "fire-soothing festival committee", "secret notes", "mini mujina",
        "razor's crude wooden crate", "a hero's mask", "yuegui", "jadevoid", "codex finalem",
        "yoimiya's candy box", "all things astrological", "church-issue journal",
        "ode to windborne wraith", "that which rises from the sea", "loom of fate",
        "the wingalet", "melusine-specialized portable integrated medical apparatus",
        "dance-off stage", "mist flower project 3, version 17, enlargement trial",
        "flamestrider", "her answer", "the seven-shifting serpent", "a hero's mask",
        "sweet pearl", "the law that walks", "character story 1", "character story 2",
        "character story 3", "character story 4", "character story 5", "letters from the audience",
        "a fontainian nursery rhyme", "old waterskin", "the wingalet", "white jade comb",
        "ya-chan and te-chan", "nahida's 'toy box'", "church-issue journal", "multipurpose front-line surveying device",
        "a legend of sword", "chess game: liyue millennial", "warning of roses"
    }

    try:
        files = sorted(os.listdir(directory))
        files = [f for f in files if f.endswith('.txt')]
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        return

    print(f"Found {len(files)} .txt files to process.")

    char_pattern = re.compile(r"^([A-Za-z][\w\s()'-]*):", re.MULTILINE)

    for filename in files:
        filepath = os.path.join(directory, filename)
        print(f"\n--- Processing: {filename} ---")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                matches = char_pattern.findall(content)
                print(f"Raw matches found: {matches}")

                for name in matches:
                    clean_name = name.split('(')[0].strip()
                    if clean_name.lower() not in EXCLUSION_LIST and len(clean_name) > 0:
                        if len(clean_name.split()) < 4:
                             all_characters.add(clean_name)
        except Exception as e:
            print(f"Error processing file {filename}: {e}")


    sorted_characters = sorted(list(all_characters))

    print("\n\n--- Final Complete Character List ---")
    for char in sorted_characters:
        print(char)
    print("-----------------------------")
    print(f"Total unique characters found: {len(sorted_characters)}")

if __name__ == "__main__":
    audit_characters()
