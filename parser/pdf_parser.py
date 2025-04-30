# parser/pdf_parser.py
import os
import pdfplumber

def get_text_from_pdf(file_path):
    """
    Extracts text from a PDF file using pdfplumber.
    Returns plain text extracted from all pages.
    """
    try:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                page_text = page.extract_text()
                if page_text:
                    text += f"\n\n--- Page {page_number} ---\n"
                    text += page_text
        return text.strip()
    
    except Exception as e:
        print(f"❌ Error reading PDF with pdfplumber: {e}")
        return None
