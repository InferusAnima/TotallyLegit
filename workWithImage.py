import pytesseract
import os
from PIL import Image
import normalizationText
tessdata_dir_config = r'--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'


def get_text(path: os.path):
    image = Image.open(path)
    text = pytesseract.image_to_string(image, lang='rus', config=tessdata_dir_config)
    return text


def check_words(text: str, words: list, islower=True):
    if islower:
        text = text.lower()
    word_counter = 0
    for word in text.split():
        if word in words:
            word_counter += 1
    return word_counter

def get_type(path: os.path):
    text = get_text(path)
    text = normalizationText.normalize(text)
    if "фактур" in text:
        return "facture"
    elif "счет" in text:
        return "bill"
    else:
        return "undefind"