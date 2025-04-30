import os
from pathlib import Path

def get_text_from_txt(file_path):
    """
    Extracts text from a .txt file. It returns paragraphs and headings.
    """
    try:
        # Open the .txt file
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # List to store extracted content
        extracted_paragraphs = []

        # Loop through each line in the file
        for line in lines:
            text = line.strip()
            if text:  # Only add non-empty lines
                extracted_paragraphs.append({
                    'style': 'Normal',
                    'text': text
                })

        # Optionally print the extracted text for debugging
        for para in extracted_paragraphs:
            print(f"Style: {para['style']}, Text: {para['text']}")

        return extracted_paragraphs

    except Exception as e:
        print(f"❌ Error reading the TXT file: {e}")
        return None