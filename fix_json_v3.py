import json

with open('trivia_questions.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line index for the start of the question 536 object
start_index = -1
for i, line in enumerate(lines):
    if '"ID": "536"' in line:
        start_index = i
        break

if start_index == -1:
    print("Error: Could not find the start of question 536.")
    exit()

# Find the closing brace for the question 536 object
end_index = -1
for i in range(start_index, len(lines)):
    if '}' in lines[i]:
        # This is the line with the closing brace.
        # Check if it already has a comma.
        if not lines[i].strip().endswith(','):
            lines[i] = lines[i].rstrip() + ',\n'
            print(f"Found closing brace on line {i+1} and added a comma.")
        else:
            print(f"Comma already exists on line {i+1}. No changes made.")
        end_index = i
        break

if end_index == -1:
    print("Error: Could not find the closing brace for question 536.")
    exit()

# Write the corrected lines back to the file
with open('trivia_questions.json', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Finished attempting to fix the JSON file.")
