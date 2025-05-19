import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os

pdf_path=input("Enter the relative path of the file (Should be in the same folder) : ")

# Important variables

pytesseract.pytesseract.tesseract_cmd=r"C:\Users\MEGH\AppData\Local\Programs\Tesseract-OCR\tesseract.exe" # Address of tesseract OCR in your system

os.makedirs(r"Images", exist_ok=True)


poppler_path=r"C:\Poppler\poppler-24.08.0\Library\bin" # Address of poppler in your system

pages = convert_from_path(pdf_path, 300, poppler_path=poppler_path)

txt_path=pdf_path[:-4]+".txt"


count=0
while os.path.exists(txt_path) :
    count+=1
    txt_path=pdf_path[:-4]+f"[{count}]"+".txt"

    

# ACTUAL CODE

try :

    for page_number, img in enumerate(pages):
        
        img.save(fr"Images\page_{page_number + 1}.png", "PNG")
        
        text = pytesseract.image_to_string(img)

        with open(txt_path,'a',encoding='utf-8') as f:
            f.write(f"Page number : {page_number+1} \n\n{text}\n")


    print(f"SUCCESS YOUR FILE {txt_path} HAS BEEN SAVED")
except Exception as e:
    print(f"An Error occured : {str(e)}")
