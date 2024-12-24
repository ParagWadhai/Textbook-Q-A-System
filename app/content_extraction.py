import PyPDF2

def extract_text_from_pdf(pdf_path):
    """Extracts text from a given PDF file."""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = []
        for page in pdf_reader.pages:
            text.append(page.extract_text())
    return "\n".join(text)

def save_extracted_texts(output_file, pdf_paths):
    """Saves extracted texts from multiple PDFs to a file."""
    extracted_texts = []
    for pdf_path in pdf_paths:
        extracted_texts.append(extract_text_from_pdf(pdf_path))
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("\n\n".join(extracted_texts))
