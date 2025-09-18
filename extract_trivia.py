import json
import re
import os

INPUT_JSON_PATH = "trivia/genshin_trivia.json" # Pointing to the original corrupted file
EXTRACTED_DATA_PATH = "trivia/extracted_data.json"

def robust_extract_data(filepath):
    """
    Extracts data from a severely malformed JSON-like file by treating it
    as text and finding objects and key-value pairs with regex.
    """
    if not os.path.exists(filepath):
        print(f"Error: File not found at '{filepath}'")
        return

    print(f"Robustly extracting data from raw text file: {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all chunks that look like JSON objects
        # This looks for content between { and }
        object_chunks = re.findall(r'\{(.*?)\}', content, re.DOTALL)

        extracted_data = []
        # Define regex for each key we need
        question_re = re.compile(r'"question":\s*"(.*?)"', re.DOTALL)
        answer_re = re.compile(r'"answer":\s*"(.*?)"', re.DOTALL)
        source_re = re.compile(r'"source":\s*"(.*?)"', re.DOTALL)

        for chunk in object_chunks:
            question_match = question_re.search(chunk)
            answer_match = answer_re.search(chunk)
            source_match = source_re.search(chunk)

            if question_match and answer_match and source_match:
                extracted_data.append({
                    "question": question_match.group(1),
                    "answer": answer_match.group(1),
                    "source": source_match.group(1)
                })

        if not extracted_data:
            print("Warning: Robust extraction failed. No data was extracted.")
            return

        print(f"Successfully extracted {len(extracted_data)} trivia items using robust method.")

        with open(EXTRACTED_DATA_PATH, 'w', encoding='utf-8') as f:
            json.dump(extracted_data, f, indent=2)

        print(f"Clean data saved to '{EXTRACTED_DATA_PATH}'")

    except Exception as e:
        print(f"An unexpected error occurred during robust extraction: {e}")

if __name__ == "__main__":
    robust_extract_data(INPUT_JSON_PATH)
