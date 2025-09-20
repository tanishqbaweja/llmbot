import json
import re
import os

def fix_trivia_json_final(input_filename="trivia_questions.json", output_filename="trivia_questions_fixed.json"):
    """
    Reads a severely malformed JSON file by isolating each object, fixing its
    internal syntax individually, and then reassembling a valid JSON array.
    This is a robust method designed to handle complex, inconsistent errors.
    """
    print(f"Attempting to fix '{input_filename}' with the definitive script...")

    if not os.path.exists(input_filename):
        print(f"Error: Input file '{input_filename}' not found.")
        return

    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # --- Start of Definitive Correction Logic ---

    # 1. Clean up the container characters and split into individual, broken object strings.
    #    The split occurs at the boundary between objects.
    content_stripped = content.strip()
    if content_stripped.startswith('[') and content_stripped.endswith(']'):
        content_stripped = content_stripped[1:-1] # Remove wrapping brackets

    # Split by the most reliable delimiter between objects: a closing brace followed by an opening one.
    # This gives us a list of "object innards".
    broken_objects = re.split(r'}\s*,?\s*{', content_stripped)

    cleaned_objects = []
    print(f"Found {len(broken_objects)} potential objects to process...")

    # 2. Loop through and fix each object string one by one.
    for i, obj_str in enumerate(broken_objects):
        # Add the curly braces back to each object string
        if i == 0 and not obj_str.strip().startswith('{'):
            fixed_str = '{' + obj_str.strip() + '}'
        elif i > 0 and not obj_str.strip().startswith('{'):
            fixed_str = '{' + obj_str.strip() + '}'
        else:
             fixed_str = obj_str.strip()
        
        # This is a critical step: some values end with a literal backslash.
        # Temporarily replace `\\",` with a unique placeholder to protect it.
        fixed_str = fixed_str.replace('\\\\",', '___BACKSLASH_QUOTE_COMMA___')

        # Now, fix the common malformed separators. This is the most complex error.
        fixed_str = fixed_str.replace('\\\", \\\"', '", "')

        # Add missing commas between key-value pairs using capture groups.
        # This looks for "value" "key" and inserts a comma.
        pattern = r'("|\d|]|true|false})\s+(")'
        replacement = r'\1,\n\2'
        fixed_str = re.sub(pattern, replacement, fixed_str)
        
        # Now it's safe to un-escape all remaining double quotes.
        fixed_str = fixed_str.replace('\\"', '"')

        # Restore the placeholder for the literal backslash case.
        fixed_str = fixed_str.replace('___BACKSLASH_QUOTE_COMMA___', '\\\\",')

        # Clean up any non-breaking spaces
        fixed_str = fixed_str.replace(u'\xa0', ' ')
        
        cleaned_objects.append(fixed_str)

    # 3. Reassemble the full JSON array string.
    final_json_string = "[\n" + ",\n".join(cleaned_objects) + "\n]"
    
    # --- End of Definitive Correction Logic ---

    print("Reassembly complete. Verifying final JSON structure...")

    try:
        # 4. Validate the final string by parsing it.
        data = json.loads(final_json_string)
        print("Verification successful! The file is now valid JSON.")

        # 5. Write the validated, formatted data to the output file.
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        print(f"Successfully created '{output_filename}'.")

    except json.JSONDecodeError as e:
        print("\n--- VERIFICATION FAILED ---")
        print("The final script could not parse the file. This indicates an unusual error.")
        print(f"JSON Error: {e}")
        # To help debug, print the context around the error
        lines = final_json_string.split('\n')
        error_line_index = e.lineno - 1
        start = max(0, error_line_index - 2)
        end = min(len(lines), error_line_index + 3)
        print("\n--- Context of Error ---")
        for i in range(start, end):
            line_num = i + 1
            prefix = ">> " if i == error_line_index else "   "
            print(f"{prefix}{line_num:4d}: {lines[i]}")
        print("-" * 20)

        print("\nSaving the failed final string to 'trivia_questions_debug.txt' for manual inspection.")
        with open("trivia_questions_debug.txt", 'w', encoding='utf-8') as f:
            f.write(final_json_string)

if __name__ == "__main__":
    fix_trivia_json_final()