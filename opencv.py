import cv2
import pandas as pd
import string
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')
print(df.head(40))
print(df.describe())
arr = list(df.text.loc[df._type == "bill"])
print(len(arr))
wordDict = dict()
allWords = set()

for i in arr:
    for x in i.replace("\n", "").split(" "):
        w = ''.join([t for t in x if not t.isdigit() and t not in string.punctuation and t != "№"])
        if len(w) > 2:
            if w in wordDict.keys():
                wordDict[w] += 1
            else:
                wordDict[w] = 1

df_word = pd.DataFrame(wordDict.values(), index=wordDict.keys(), columns=["data"])
df_word.sort_values(df_word.columns[0], inplace=True, ascending=False)

d = df_word.loc[(df_word.data > 30)]
print(d.head(20))
plt.bar(range(len(d)), d.data, tick_label=d.index)
plt.xticks(rotation=90)
plt.show()
