import pytesseract
from PIL import Image

def ocr_based_grading(image_path):
   
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    
    return text
