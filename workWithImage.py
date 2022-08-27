import pytesseract
import os
from PIL import Image
import re
import nltk
from nltk.corpus import stopwords
tessdata_dir_config = r'--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'
nltk.download('stopwords')

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


def normalize(string:str):


    snowball = nltk.SnowballStemmer(language="russian")
    stop_words = set(stopwords.words('russian'))

    lower_string = string.lower()
    no_number_string = re.sub(r'\d+', '', lower_string)
    no_punc_string = re.sub(r'[^\w\s]', '', no_number_string)
    no_wspace_string = no_punc_string.strip()
    lst_string = [no_wspace_string][0].split()
    no_stpwords_string = ""
    for i in lst_string:
        if i not in stop_words:
            no_stpwords_string += i + ' '

    no_stpwords_string = no_stpwords_string[:-1]

    l = ""
    for i in no_stpwords_string.split(" "):
        l += snowball.stem(i) + " "

    return l[:-1]


def get_type(path: os.path):
    text = get_text(path)
    text = normalize(text)

    if "фактур" in text:
        print(text,"facture")
        return "счет-фактура"
    elif "счет на оплат" in text:
        print(text,"bill_to_pay")
        return "счет"
    elif "сче" in text and not ("акт" in text) and not ("отче" in text) and not ("орде" in text):
        print(text,'bill')
        return "счет"
    return "другое"
