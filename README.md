# 📁 Doc Formatter – Console-Based Document Standardizer

##
| Summary                                                           |
|-----------------------------------------------------------------|
|This project's intent is to automate the process of standardizing the test procedures that we get from the cleint, into the EMS ISO controled documents. |
 


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
