# 📄 PDF to Text Converter (OCR)

This project is a simple and effective **PDF to Text Extractor** that uses **Tesseract OCR** to convert scanned or image-based PDFs into editable `.txt` files.

Built with **pytesseract + pdf2image** for OCR processing.

---

## 🚀 Features

- Upload any image-based or scanned PDF
- Convert each page into high-resolution images
- Use OCR to extract text from the images
- Save the extracted text instantly as a `.txt` file
- Automatically skips duplicate processing if the same file was already handled

---

## 🛠️ Installation
Download Tesseract OCR and Popple for image handling
Create and activate virtual Enviroment as well
<b><u> Copy the relative path into the folder and change file names in App.py to use it by giving the relative path </b></u>

### 1. Clone the Repository

```bash
git clone https://github.com/MeghPatel2810/pdf-to-text-ocr.git
cd pdf-to-text-ocr
pip install -r requirements.txt