from pytesseract import pytesseract
from PIL import Image

# 엔진
img = Image.open("./source/news.png")
# img = Image.open("./source/coffee-blue.jpg")
pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
# img.show()
text = pytesseract.image_to_string(img, lang='kor+eng')
print(text.replace("",""))

# 변환된 텍스트를 파일에 쓰기
# encoding='utf-8' 꼭 명시해야함
with open("./output/news.text",'w',encoding='utf-8') as f:
    f.write(text.replace(" ",""))

    f.close()

