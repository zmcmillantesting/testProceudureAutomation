import os
from parser.docx_parser import get_text_from_docx
from parser.txt_parser import get_text_from_txt
from parser.pdf_parser import get_text_from_pdf
from formatter.standardizer import apply_standard_formatting

def main():
    filename = input("Enter full file name e.g. example.txt or example.pdf: ")
    process_file(filename)

def process_file(filename):
    input_path = os.path.join("input_docs", filename)
    output_filename = f"standardized_{os.path.splitext(filename)[0]}.docx"
    output_path = os.path.join("standardized_docs", output_filename)

    # Ensure output directory exists
    os.makedirs("standardized_docs", exist_ok=True)

    if os.path.exists(input_path):
        print(f"Processing file: {filename}")
        
        if filename.endswith(".docx"):
            extracted_text = get_text_from_docx(input_path)
            if extracted_text:
                print("Successfully extracted text from DOCX file")
                apply_standard_formatting(extracted_text, "Programming_content.docx", output_path)
        
        elif filename.endswith(".txt"):
            extracted_text = get_text_from_txt(input_path)
            if extracted_text:
                print("Successfully extracted text from TXT file")
                apply_standard_formatting(extracted_text, "Programming_content.docx", output_path)
        
        elif filename.endswith(".pdf"):
            extracted_text = get_text_from_pdf(input_path)
            if extracted_text:
                print("Successfully extracted text from PDF file")
                apply_standard_formatting(extracted_text, "Programming_content.docx", output_path)
        else:
            print("Unsupported file type. Please use .txt, .docx, or .pdf files.")
    else:
        print("File not found. Please check the file name and try again.")

if __name__ == "__main__":
    main()

