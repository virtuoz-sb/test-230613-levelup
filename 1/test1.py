import camelot
import PyPDF2
import re

def extract_date(pdf_path):
    # Extract text from PDF using PyPDF2
    with open(pdf_path, "rb") as f:
        pdf = PyPDF2.PdfFileReader(f)
        num_pages = pdf.numPages
        pages_text = []
        for page_num in range(num_pages):
            page = pdf.getPage(page_num)
            text = page.extractText()
            pages_text.append(text)

    # Load PDF using camelot
    tables = camelot.read_pdf(pdf_path, pages="all")

    # Find the table containing the desired rows and columns
    table = None
    for t in tables:
        if "POLICY EFF" in t.df.columns and "POLICY EXP" in t.df.columns:
            table = t
            break

    if table is None:
        print("Table not found. Please check the PDF format or table structure.")
        return

    # Extract the dates from the specified rows and columns
    dates = []
    for i in range(start_row, end_row):
        row_data = table.df.loc[i, [start_col, end_col]].tolist()
        row_dates = []
        for cell in row_data:
            matches = re.findall(r"\d{2}/\d{2}/\d{4}", cell)
            if matches:
                row_dates.append(matches[0])
            else:
                row_dates.append("Date not found")
        dates.append(row_dates)

    # Print the extracted dates
    for i, date in enumerate(dates, start=1):
        print(f"ROW {chr(64+i)}: {date[0]} to {date[1]}")