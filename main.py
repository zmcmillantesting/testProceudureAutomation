import os
from parser.docx_parser import get_text_from_docx
print("import from docx_parser success")
from parser.txt_parser import get_text_from_txt
print("import from txt_parser success")
from parser.pdf_parser import get_text_from_pdf
print("import from pdf_parser success")

# from pdf import PDF

def main():
    filename = input("Enter full file name e.g. example.txt or example.pdf: ")
    get_file_path(filename)
    # filePath = "input_docs/" + filename


def get_file_path(filename):
    filePath = "input_docs/" + filename

    if os.path.exists(filePath):
        print("File found.")
        if filename.endswith(".docx"):
            extracted_text = get_text_from_docx(filePath)
            if extracted_text:
                print("Extracted text from DOCX file:")
                for para in extracted_text:
                    print(f"Style: {para['style']}, Text: {para['text']}")
        elif filename.endswith(".txt"):
            extracted_text = get_text_from_txt(filePath)
            if extracted_text:
                print("Extracted text from TXT file:")
                print(extracted_text)  # Print plain text directly
        elif filename.endswith(".pdf"):
            extracted_text = get_text_from_pdf(filePath)
            if extracted_text:
                print("Extracted text from PDF file:")
                print(extracted_text)  # Print plain text directly
    else:
        print("File not found. Please check the file name and try again.")


if __name__ == "__main__":
    main()

