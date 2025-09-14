import json

# This is a bit of a hacky script to fix a known JSON syntax error.
# The `trivia_questions.json` file is missing a comma after the object for question 536.
# This script will read the file line by line, and when it finds the end of the object for question 536,
# it will add the missing comma.

with open('trivia_questions.json', 'r') as f:
    lines = f.readlines()

output_lines = []
found_question_536 = False
in_question_536 = False

for line in lines:
    if '"ID": "536"' in line:
        found_question_536 = True
        in_question_536 = True

    if in_question_536 and '}' in line:
        # This is the end of the object for question 536.
        # Add a comma to the line.
        line = line.strip() + ',\n'
        in_question_536 = False

    output_lines.append(line)

with open('trivia_questions.json', 'w') as f:
    f.writelines(output_lines)

print("Attempted to fix the JSON file by adding a missing comma after question 536.")
