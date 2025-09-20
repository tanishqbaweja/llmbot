import re

with open('trivia/trivia_questions.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the malformed structure by replacing the concatenated fields
content = re.sub(r'"([^"]+)"\s*,\s*\\"([^"]+)"\s*:\s*"([^"]*)"', r'"\1",\n        "\2": "\3"', content)

# Fix remaining patterns
content = re.sub(r'\\"([^"]+)"\s*:\s*"([^"]*)"', r'"\1": "\2"', content)

with open('trivia/trivia_questions.json', 'w', encoding='utf-8') as f:
    f.write(content)

print("Rebuilt JSON structure")