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

if __name__ == "__main__":
    files_to_convert = [
        "O.docx", "Q.docx", "R.docx", "S.docx", "T.docx",
        "V.docx", "W.docx", "X.docx", "Y.docx"
    ]

    for filename in files_to_convert:
        docx_path = f"GenshinStories/{filename}"
        txt_path = f"GenshinStories/{filename.replace('.docx', '_converted.txt')}"
        try:
            docx_to_txt(docx_path, txt_path)
        except Exception as e:
            print(f"Could not convert {docx_path}: {e}")
