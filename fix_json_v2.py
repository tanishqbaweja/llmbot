import json

try:
    with open('trivia_questions.json', 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("Error: trivia_questions.json not found.")
    exit()

# The error is a missing comma after the object for question 536.
# This is a targeted fix for that specific issue.
# The string to search for is the end of the explanation for question 536,
# followed by the closing brackets of that object.

# I will find the specific pattern that marks the end of the object for question 536
# and manually insert a comma if it's missing.

# The end of the explanation for Q536
end_of_explanation = '"The Arab Spring was a series of anti-government protests and uprisings that spread across much of the Arab world in the early 2010s. It began in Tunisia in response to oppressive regimes and a low standard of living."'

# The full block to find is the end of the explanation and the closing curly brace
# of the object, without a comma before the next object.
block_to_find = end_of_explanation + '\n  }\n  {\n    "ID": "IND1"'

# The corrected block will have a comma added.
corrected_block = end_of_explanation + '\n  },\n  {\n    "ID": "IND1"'

if block_to_find in content:
    content = content.replace(block_to_find, corrected_block)

    with open('trivia_questions.json', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully found the problematic block and inserted a comma.")
else:
    # It seems my previous attempts to fix it might have partially worked,
    # or the search string is wrong. Let's try to be less specific.
    block_to_find_alt = '"explanation": "The Arab Spring was a series of anti-government protests and uprisings that spread across much of the Arab world in the early 2010s. It began in Tunisia in response to oppressive regimes and a low standard of living."\n  }'
    corrected_block_alt = block_to_find_alt + ','

    if block_to_find_alt in content:
        content = content.replace(block_to_find_alt, corrected_block_alt)

        with open('trivia_questions.json', 'w', encoding='utf-8') as f:
            f.write(content)

        print("Successfully found the problematic block (alternate) and inserted a comma.")
    else:
        print("Could not find the specific syntax error. The file may have a different issue or the error is elsewhere.")
