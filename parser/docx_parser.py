# parser/docx_parser.py
from docx import Document

def get_text_from_docx(file_path):
    """
    Extracts text from a .docx file. It returns paragraphs and headings.
    """
    try:
        # Open the .docx file
        document = Document(file_path)
        
        # List to store extracted content
        extracted_paragraphs = []

        # Loop through each paragraph in the document
        for para in document.paragraphs:
            text = para.text.strip()
            if text:  # Only add non-empty paragraphs
                style = para.style.name
                extracted_paragraphs.append({
                    'style': style,
                    'text': text
                })

        # Optionally print the extracted text for debugging
        for para in extracted_paragraphs:
            print(f"Style: {para['style']}, Text: {para['text']}")

        return extracted_paragraphs
    
    except Exception as e:
        print(f"❌ Error reading the DOCX file: {e}")
        return None



