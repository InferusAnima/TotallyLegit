import workWithImage
import os


path = "dataset/other"
for i in os.listdir(path):
    if "jpg" in i:
        text = workWithImage.get_text(f"{path}/{i}")
        f = open(f"text_{path}/{i.replace('.jpg','.txt')}","w",encoding="utf-8")
        f.write(text)
        f.close()
        print(i,workWithImage.normalize(text))