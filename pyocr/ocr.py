# 이미지 처리 - Pillow
from PIL import Image
from pytesseract import pytesseract

# 엔진
pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
img = Image.open("source/news.png")
# img.show()
text = pytesseract.image_to_string(img, lang='kor')
print(text)

