import json

try:
    with open('trivia_questions.json', 'r', encoding='utf-8') as f:
        # Read the file content and find the position to truncate
        content = f.read()

        # Find the end of the explanation for question 524
        # This is the last known good entry
        search_string = '"explanation": "The Detroit Red Wings are a professional ice hockey team (NHL) based in Detroit and one of the league\'s \'Original Six\'. The Pistons play basketball, the Tigers play baseball, and the Lions play American football."'

        last_good_pos = content.find(search_string)
        if last_good_pos == -1:
            print("Error: Could not find the last known good question (ID 524). Cannot revert.")
            exit()

        # Find the closing brace of that object
        closing_brace_pos = content.find('}', last_good_pos)
        if closing_brace_pos == -1:
            print("Error: Could not find the closing brace for the last known good question. Cannot revert.")
            exit()

        # Truncate the content to that point
        truncated_content = content[:closing_brace_pos + 1]

        # Re-append the closing bracket for the JSON list
        final_content = truncated_content + '\n]\n'

    # Overwrite the file with the reverted content
    with open('trivia_questions.json', 'w', encoding='utf-8') as f:
        f.write(final_content)

    print("Successfully reverted trivia_questions.json to its last known good state (after question 524).")

except Exception as e:
    print(f"An unexpected error occurred during the revert process: {e}")
