# formatter/standardizer.py

from docx import Document
import os
from .template_loader import TemplateLoader

def apply_standard_formatting(source_text, template_path, output_path):
    """
    Inserts extracted text into a standard DOCX template and saves it.
    
    Parameters:
    - source_text (str or list): Text extracted from the original file.
    - template_path (str): Path to the standard template DOCX.
    - output_path (str): Path to save the formatted document.
    """
    try:
        # Convert template path to absolute path
        template_full_path = os.path.join("templates", template_path)
        print(f"Loading template from: {template_full_path}")
        
        # First structure the content into organized fields
        structured_data = structure_content(source_text)
        print("Structured content:", structured_data)
        
        # Use the template loader to properly insert content
        template = TemplateLoader(template_full_path)
        doc = template.insert_data(structured_data)
        
        if doc:
            # Save the new standardized document
            print(f"Saving document to: {output_path}")
            template.save_document(output_path, doc)
            print(f"✅ Document standardized and saved to {output_path}")
            return True
        else:
            print("❌ Failed to insert data into template")
            return False

    except Exception as e:
        print(f"❌ Error formatting document: {e}")
        return False

def structure_content(source_text):
    """
    Structures the source text into a format suitable for template insertion.
    
    Parameters:
    - source_text (str or list): Raw text from parser
    
    Returns:
    - dict: Structured data ready for template insertion
    """
    data = {
        'title': '',
        'procedure_number': '',
        'revision': '',
        'content': '',
        'date': '',
        'author': ''
    }
    
    if isinstance(source_text, list):
        # Handle structured input (e.g., from docx_parser)
        content_parts = []
        for block in source_text:
            text = block['text']
            # Try to identify and extract metadata
            if 'title' in block.get('style', '').lower():
                data['title'] = text
            elif 'heading' in block.get('style', '').lower():
                if not data['title']:  # Use first heading as title if no title style found
                    data['title'] = text
            else:
                content_parts.append(text)
        data['content'] = '\n'.join(content_parts)
    else:
        # Handle plain text input (e.g., from pdf or txt parser)
        lines = source_text.split('\n')
        if lines:
            data['title'] = lines[0]  # Use first line as title
            data['content'] = '\n'.join(lines[1:])  # Rest as content
    
    return data
