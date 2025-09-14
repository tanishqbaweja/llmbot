import json

try:
    with open('trivia_questions.json', 'r', encoding='utf-8') as f:
        json.load(f)
    print("JSON is already valid. No changes made.")
except json.JSONDecodeError as e:
    print(f"JSON is invalid. Error: {e}")
    print("Attempting a brute-force fix...")

    with open('trivia_questions.json', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the last closing brace and insert a comma before the closing bracket
    # This is a common error when concatenating JSON objects into a list.
    last_brace_index = content.rfind('}')
    if last_brace_index != -1:
        # Find the next character that is not whitespace
        next_char_index = -1
        for i in range(last_brace_index + 1, len(content)):
            if not content[i].isspace():
                next_char_index = i
                break

        if next_char_index != -1 and content[next_char_index] == ']':
            # This is the case where the last object is not followed by a comma
            # before the closing bracket of the list.
            # Let's add a comma after the last brace.
            # But since this might be the last element, we should remove the comma before the final ']'
            # The error is likely a missing comma between two objects, not at the end of the list.
            # I will try a different approach. I will find the line with the error and fix it.

            error_line = e.lineno
            with open('trivia_questions.json', 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # The error is "Expecting ',' delimiter". This means a comma is missing.
            # I will add a comma to the end of the previous line.
            if error_line > 1:
                lines[error_line - 2] = lines[error_line - 2].rstrip() + ',\n'

                with open('trivia_questions.json', 'w', encoding='utf-8') as f:
                    f.writelines(lines)

                print(f"Added a comma to line {error_line - 1}.")
            else:
                print("Cannot fix error on the first line.")
        else:
            print("Could not find the expected pattern of a missing comma before the final bracket.")
    else:
        print("Could not find any closing braces.")
