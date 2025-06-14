# PDF Invoice Extractor

This project is a **Python-based utility** to extract key information from Amazon and Flipkart invoice PDFs and save the structured data to an Excel file.  
It uses **PyMuPDF (fitz)** for PDF parsing — no third-party APIs, so all data stays local and secure.

---

## 📂 Project Structure

pdf-invoice-extractor/
├── main.py # Main Python script for extraction and Excel export

├── fk_invoice_1.pdf # Sample Flipkart invoice (for testing)

├── fk_invoice_2.pdf # Sample Flipkart invoice (for testing)

├── output/

│ └── invoice_data.xlsx # Extracted data saved in Excel format

## ⚙ Features

✅ Extracts **Invoice Number**, **Invoice Date**, **Total Amount**, and **GSTIN**  
✅ Handles both **Amazon** and **Flipkart** invoices  
✅ Saves data to **Excel (.xlsx)**  
✅ Hard-coded logic — no external API calls  
✅ Simple, lightweight solution

---

## 🚀 How to Run

### 1️⃣ Install dependencies
```bash
pip install PyMuPDF openpyxl
2️⃣ Run the script
bash
Copy
Edit
python main.py
By default, it looks for PDF files in the same directory or as specified in the code. The extracted data will be saved to:



