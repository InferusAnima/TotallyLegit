import PIL.Image
import pandas as pd
import pytesseract
import config
from PIL import Image

tessdata_dir_config = r'--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'

arr = []
texts = []
types = []

def detect(i: PIL.Image.Image):
    text = pytesseract.image_to_string(i, lang='rus', config=tessdata_dir_config).lower()
    if "счет" in text and "фактура" in text:
        return text, "facture"
    elif "счет" in text фи:
        return text, "bill_to_pay"
    elif "счет №" in text:
        return text, "bill"
    else:
        return text, "None"
    score_f = 0
    score_btp = 0
    score_b = 0

    for i in config.facture.keys():
        if i in text:
            score_f += config.facture[i]
    for i in config.bill_to_pay.keys():
        if i in text:
            score_btp += config.bill_to_pay[i]
    for i in config.bill.keys():
        if i in text:
            score_b += config.bill[i]

    if max(score_b, score_f, score_btp) == score_b:
        return text, score_b, "bill"
    if max(score_b, score_f, score_btp) == score_btp:
        return text, score_btp, "bill_to_pay"
    if max(score_b, score_f, score_btp) == score_f:
        return text, score_f, "facture"
    return text, 0, "None"


for i in range(317):
    text, _type = detect(Image.open(f'images\inv-{i:04}.jpg'))
    arr.append(f'images\inv-{i:04}.jpg')
    texts.append(text)
    types.append(_type)

df = pd.DataFrame(data=dict(imgs=arr,text=texts,_type=types))
print(df.head())
df.to_csv("dataset.csv")