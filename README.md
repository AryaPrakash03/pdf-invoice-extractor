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

output/invoice_data.xlsx
📝 Sample Extracted Fields
File	Invoice Number	Invoice Date	Total Amount	GSTIN
fk_invoice_1.pdf	FAR1RI2600007537	NOT FOUND	249.00	19ATNPP2571M1ZW
fk_invoice_2.pdf	(Your data here)	(Your data)	(Your data)	(Your data)
amz_invoice_1.pdf	(Your data here)	(Your data)	(Your data)	(Your data)

💡 How It Works
👉 The script uses regular expressions on extracted PDF text to locate patterns like:

Invoice Number

Invoice Date

Grand Total

GSTIN

👉 The data is collected into a list of dictionaries and written to Excel using openpyxl / pandas.

🛑 Limitations
⚠ The current version relies on hard-coded patterns. It may fail if:

The invoice format changes

The PDF text is non-searchable (scanned image without OCR)

📈 Future Improvements
✅ Add support for scanned invoices using OCR (e.g., Tesseract)
✅ Make field detection dynamic and configurable
✅ Build a CLI or GUI around it


📄 License
This project is open-source and free to use under the MIT License.
### 🚀 **Next Steps**
👉 Save this as `README.md` in your project folder:
```bash
echo "<paste content here>" > README.md
git add README.md
git commit -m "Add detailed README"
git push
