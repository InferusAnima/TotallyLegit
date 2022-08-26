import os
import PIL.Image
import pytesseract
from PIL import Image
import shutil

tessdata_dir_config = r'--tessdata-dir "/usr/local/Cellar/tesseract/5.2.0/share/tessdata/"'

arr = []


def detect(i: PIL.Image.Image):
    text = pytesseract.image_to_string(i, lang='rus', config=tessdata_dir_config).lower()
    if "счет" in text and "фактура" in text:
        return text, "facture"
    elif "счет" in text:
        return text, "bill"
    else:
        return text, "other"


os.mkdir('./dataset/new')

for i in range(118):
    file = f'images/{i}.jpeg'
    img = Image.open(file)
    text, _type = detect(img)
    arr.append(file)
    if not os.path.isdir(f'./dataset/new/{_type}'):
        os.mkdir(f'./dataset/new/{_type}')
    rgb_img = img.convert('RGB')
    rgb_img.save(f'./dataset/new/{_type}/{i}.jpg')
    print(i)
