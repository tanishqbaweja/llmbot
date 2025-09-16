import json

# Load the trivia questions from the JSON file
with open('anime_trivia.json', 'r') as f:
    questions = json.load(f)

# Define the new explanations for the fourth batch
new_explanations = {
    41: "The story of 'Gosick' is set in the fictional European country of Saubure, and the main characters attend the prestigious St. Marguerite Academy. The academy, with its vast library and old-world architecture, serves as the primary setting for the many mysteries that the protagonists, Kazuya Kujo and Victorique de Blois, solve throughout the series."
}

# Update the explanations for the questions in the batch
for question in questions:
    if question['id'] in new_explanations:
        question['explanation'] = new_explanations[question['id']]

# Write the updated data back to the JSON file
with open('anime_trivia.json', 'w') as f:
    json.dump(questions, f, indent=4)

print("Explanations for batch 4 updated successfully.")
