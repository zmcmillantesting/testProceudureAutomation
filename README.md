# 📁 Doc Formatter – Console-Based Document Standardizer

##
| Summary                                                           |
|-----------------------------------------------------------------|
|This project's intent is to automate the process of standardizing the test procedures that we get from the cleint, into the EMS ISO controled documents. |

--- 

## 🔄 Workflow Overview

1. Place raw files into `input_docs/`
2. Run `main.py` and choose the file to process
3. File is parsed by the appropriate module (`docx`, `pdf`, etc.)
4. Extracted text is passed to the formatter
5. Formatter applies rules + loads the template
6. Standardized file is saved to `output/standardized_docs/`

---

## 🖥️ Usage

- $ python main.py
- Enter full file name (e.g., test.docx, test.pdf): test.docx
- ✅ File parsed successfully.
- 📁 Standardized document saved to output/standardized_docs/test_standardized.docx

---

## 🧰 Tech Stack

| Purpose                         | Technology / Library       |
|----------------------------------|----------------------------|
| Programming Language             | Python                     |
| DOCX File Parsing                | `python-docx`              |
| PDF File Parsing                 | `PyMuPDF` (`fitz`) or `pdfplumber` |
| Excel Support (if needed)       | `openpyxl`, `pandas`       |
| Text Cleanup / Formatting       | `re` (regex)               |
| Template-Based Output           | `python-docx` or `Jinja2`  |
| File & Directory Operations     | `os`, `pathlib`, `shutil`  |

---

## 🗂️ Project Structure

| Path / File                        | Purpose                                      |
|-----------------------------------|----------------------------------------------|
| `main.py`                         | Entry point for the CLI application          |
| `parser/`                         | Folder for file parsing modules              |
| `parser/docx_parser.py`           | Extracts text from `.docx` documents         |
| `parser/pdf_parser.py`            | Extracts text from `.pdf` files              |
| `formatter/`                      | Folder for formatting and templating logic   |
| `formatter/standardizer.py`       | Applies formatting rules and templates       |
| `formatter/template_loader.py`    | Loads company-standard document template     |
| `templates/`                      | Holds standard output templates              |
| `templates/standard_template.docx`| The base template for output formatting      |
| `input_docs/`                     | Folder where raw client files are placed     |
| `output/standardized_docs/`       | Folder for saving reformatted output files   |


---

## ✅ Best Practices

- Modular design: isolate parsing, formatting, and file operations.
- Add logging for traceability (`logging` module).
- Batch process files in `input_docs/`.
- Create test files to validate different document types and edge cases.
- Store config and formatting rules in external JSON/YAML files if customization is needed.
- Use version control with a `.gitignore` for `output/`, logs, etc.
