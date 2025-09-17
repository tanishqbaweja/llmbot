import os
import docx

def convert_docx_to_txt():
    """
    Converts all .docx files in the GenshinStories directory to .txt files
    in a new GenshinStories_txt directory.
    """
    if not os.path.exists("GenshinStories"):
        print("Error: GenshinStories directory not found.")
        return

    if not os.path.exists("GenshinStories_txt"):
        os.makedirs("GenshinStories_txt")

    for filename in os.listdir("GenshinStories"):
        if filename.endswith(".docx"):
            filepath = os.path.join("GenshinStories", filename)
            document = docx.Document(filepath)
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            txt_filepath = os.path.join("GenshinStories_txt", txt_filename)

            with open(txt_filepath, "w", encoding="utf-8") as txt_file:
                for para in document.paragraphs:
                    txt_file.write(para.text + "\\n")
            print(f"Converted {filename} to {txt_filename}")

if __name__ == "__main__":
    convert_docx_to_txt()
