import fitz  # PyMuPDF
import re
import os
import pandas as pd

def extract_invoice_data(pdf_path):
    print(f"[INFO] Processing file: {os.path.basename(pdf_path)}")

    doc = fitz.open(pdf_path)
    text = ""
    
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()

    # Extract Invoice Number
    invoice_no = re.search(r'Invoice Number\s*#\s*([A-Z0-9]+)', text)

    # Extract Invoice Date (handle newline and space)
    invoice_date = re.search(r'Invoice Date[:\s]*\n*\s*([0-9\-]+)', text)

    # Extract Grand Total
    total_amount = re.search(r'Grand Total\s*₹\s*([\d,.]+)', text)

    # Extract GSTIN
    gstin = re.search(r'GSTIN\s*-\s*([0-9A-Z]+)', text)

    data = {
        'File': os.path.basename(pdf_path),
        'Invoice Number': invoice_no.group(1) if invoice_no else 'NOT FOUND',
        'Invoice Date': invoice_date.group(1) if invoice_date else 'NOT FOUND',
        'Total Amount': total_amount.group(1) if total_amount else 'NOT FOUND',
        'GSTIN': gstin.group(1) if gstin else 'NOT FOUND'
    }

    print(f"File: {data['File']}")
    print(f"Invoice Number: {data['Invoice Number']}")
    print(f"Invoice Date: {data['Invoice Date']}")
    print(f"Total Amount: {data['Total Amount']}")
    print(f"GSTIN: {data['GSTIN']}")
    print()

    return data

def main():
    input_files = [
        'fk_invoice_1.pdf','fk_invoice_2.pdf',
        # Add other files here when available
    ]

    all_data = []
    for file_path in input_files:
        if os.path.exists(file_path):
            data = extract_invoice_data(file_path)
            all_data.append(data)
        else:
            print(f"[ERROR] File not found: {os.path.abspath(file_path)}")

    # Save to Excel
    if all_data:
        df = pd.DataFrame(all_data)
        output_file = 'output/invoice_data.xlsx'
        
        # Ensure output folder exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        df.to_excel(output_file, index=False)
        print(f"[SUCCESS] Data saved to {output_file}")
    else:
        print("[WARNING] No data to save.")

if __name__ == "__main__":
    main()
