import os
from docx import Document

def docx_to_txt(docx_path, txt_path):
    """
    Converts a .docx file to a .txt file.
    """
    try:
        doc = Document(docx_path)
        full_text = [para.text for para in doc.paragraphs]
        text_content = "\n".join(full_text)
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text_content)
        print(f"Successfully converted '{docx_path}' to '{txt_path}'")
    except Exception as e:
        print(f"Error converting '{docx_path}': {e}")

def convert_all_docx_in_folder(folder_path):
    """
    Converts all .docx files in a given folder to .txt files.
    """
    if not os.path.isdir(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        return

    for filename in os.listdir(folder_path):
        if filename.endswith(".docx"):
            docx_path = os.path.join(folder_path, filename)
            txt_path = os.path.join(folder_path, os.path.splitext(filename)[0] + ".txt")
            docx_to_txt(docx_path, txt_path)

if __name__ == "__main__":
    genshin_stories_folder = "GenshinStories"
    convert_all_docx_in_folder(genshin_stories_folder)
