import json
import re

def fix_json_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix the specific id errors
    content = content.replace('"id":- "', '"id": "')
    content = content.replace('"id":= "', '"id": "')
    content = content.replace('",\n', '",')
    content = content.replace('"\n', '"')
    # Find all json objects in the string
    # A json object starts with { and ends with }
    # I will use regex to find all of them.
    json_objects_str = re.findall(r'\{[^}]*\}', content)

    json_objects = []
    for obj_str in json_objects_str:
        try:
            json_objects.append(json.loads(obj_str))
        except json.JSONDecodeError as e:
            print(f"Error decoding object: {e}")
            print(obj_str)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(json_objects, f, indent=4)

    print(f"Fixed {filepath}")

if __name__ == "__main__":
    fix_json_file("trivia/genshin_trivia_22.json")
