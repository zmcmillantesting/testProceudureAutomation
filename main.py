import os
from parser.docx_parser import get_text_from_docx
from parser.txt_parser import get_text_from_txt
from parser.pdf_parser import get_text_from_pdf
# from pdf import PDF

def main():
    filename = input("Enter full file name e.g. example.txt or example.pdf: ")


def get_file_path(filename):
    filePath = "input_docs/" + filename
    if os.path.exists(filePath):
        if filename.endswith(".docx"):
            extracted_text = get_text_from_docx(filePath)
            if extracted_text:
                print("Extracted text from DOCX file:")
                for para in extracted_text:
                    print(f"Style: {para['style']}, Text: {para['text']}")
        elif filename.endswith(".txt"):
            if filename.endswith(".txt"):
                extracted_text = get_text_from_txt(filePath)
                if extracted_text:
                    print("Extracted text from TXT file:")
                    for para in extracted_text:
                        print(f"Style: {para['style']}, Text: {para['text']}")
        elif filename.endswith(".pdf"):
            if os.path.exists(filePath):
                extracted_text = get_text_from_pdf(filePath)
                if extracted_text:
                    print("Extracted text from PDF file:")
                    for para in extracted_text:
                        print(f"Text: {para['style']}, Text: {para['text']}")

    else:
        print("File not found. Please check the file name and try again.")
        return None      


if __name__ == "__main__":
    main()

