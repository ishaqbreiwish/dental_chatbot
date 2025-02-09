from PyPDF2 import PdfReader
import os

text = ""
folder_path = "documents"

for filename in os.listdir(folder_path):
    curr_file = os.path.join(folder_path, filename)
    if filename.endswith(".pdf"):
        with open(curr_file, "rb") as pdf_file:
            reader = PdfReader(pdf_file)

            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()

output_file = "output.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(text)