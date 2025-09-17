import os
from docx import Document

def docx_to_txt(docx_path, txt_path):
    # Load the docx file
    doc = Document(docx_path)

    # Extract all text
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)

    # Join with newlines
    text_content = "\n".join(full_text)

    # Save as txt file
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text_content)

    print(f"Converted '{docx_path}' to '{txt_path}'")

def convert_all_docx_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".docx"):
            docx_path = os.path.join(directory, filename)
            txt_path = os.path.join(directory, filename.replace(".docx", ".txt"))
            docx_to_txt(docx_path, txt_path)

if __name__ == "__main__":
    convert_all_docx_in_directory("GenshinStories/")
