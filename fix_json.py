import demjson3
import json
import os

INPUT_JSON_PATH = "trivia/genshin_trivia_22.json"

def fix_json_file_with_demjson(filepath):
    """
    Uses the demjson3 library to leniently parse a malformed JSON file
    and then writes it back in a strict, valid format using the standard
    json library.
    """
    if not os.path.exists(filepath):
        print(f"Error: File not found at '{filepath}'")
        return

    print(f"Attempting to fix JSON file using demjson3: {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # demjson3 can decode json that has some syntax errors
        decoded_data = demjson3.decode(content)

        # Now, write it back using the standard json library to enforce strict syntax
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(decoded_data, f, indent=2) # Use indent=2 for readability

        print("Successfully parsed and re-wrote the JSON file. It should now be valid.")

    except demjson3.JSONDecodeError as e:
        print(f"demjson3 failed to decode the file. The file may be severely corrupted. Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    fix_json_file_with_demjson(INPUT_JSON_PATH)
