import camelot
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import re

def get_policy_number(X, pdf_path):
    # Convert PDF pages to images
    images = convert_from_path(pdf_path)

    # Perform OCR on each image and extract text
    pages_text = []
    for image in images:
        text = pytesseract.image_to_string(image)
        pages_text.append(text)

    # Load PDF using camelot with OCR text
    tables = camelot.read_pdf(pdf_path, pages="all", table_areas=['0,700,595,0'], process_background=True, recognition="ocr")

    # Find the table containing the desired rows and columns
    table = None
    for t in tables:
        if "POLICY" in t.df.columns and "NUMBER" in t.df.columns:
            table = t
            break

    if table is None:
        print("Table not found. Please check the PDF format or table structure.")
        return

    # Find the policy number for the given input
    policy_number = None
    for i, row in table.df.iterrows():
        if X in row.values:
            policy_number = row[table.df.columns[1]]  # Assuming policy number is in the second column
            break

    if policy_number is None:
        print(f"Policy number not found for {X}.")
    else:
        return policy_number

# Usage example
pdf_path = "test2.pdf"
print("get_policy_number(A) =>", get_policy_number("A", pdf_path))
print("get_policy_number(B) =>", get_policy_number("B", pdf_path))
print("get_policy_number(C) =>", get_policy_number("C", pdf_path))
print("get_policy_number(D) =>", get_policy_number("D", pdf_path))