import pdfplumber
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

if __name__ == "__main__":
    # Name of your PDF file
    pdf_name = "sample.pdf"  # Change to your PDF file name
    input_path = os.path.join("..", "data", pdf_name)
    output_path = os.path.join("..", "outputs", pdf_name.replace(".pdf", ".txt"))

    text = extract_text_from_pdf(input_path)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    
    print(f"Extracted text written to {output_path}")
