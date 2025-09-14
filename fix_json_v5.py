error_line = 6969
try:
    with open('trivia_questions.json', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if error_line > 1 and len(lines) >= error_line -1 :
        # The line that needs the comma is the one before the error.
        line_to_fix_index = error_line - 2

        # Add comma to the end of the line, preserving original whitespace
        lines[line_to_fix_index] = lines[line_to_fix_index].rstrip() + ',\n'

        with open('trivia_questions.json', 'w', encoding='utf-8') as f:
            f.writelines(lines)

        print(f"Force-added a comma to the end of line {error_line - 1}.")
    else:
        print("Error: Line number is out of range or file is too short.")

except FileNotFoundError:
    print("Error: trivia_questions.json not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
