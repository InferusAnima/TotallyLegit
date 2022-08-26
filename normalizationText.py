import re

# download stpwords
import nltk

nltk.download('stopwords')
snowball = nltk.SnowballStemmer(language="russian")
# import nltk for stopwords
from nltk.corpus import stopwords

stop_words = set(stopwords.words('russian'))

def normalize(string:str):
    lower_string = string.lower()
    no_number_string = re.sub(r'\d+', '', lower_string)
    no_punc_string = re.sub(r'[^\w\s]', '', no_number_string)
    no_wspace_string = no_punc_string.strip()
    lst_string = [no_wspace_string][0].split()
    no_stpwords_string = ""
    for i in lst_string:
        if not i in stop_words:
            no_stpwords_string += i + ' '

    no_stpwords_string = no_stpwords_string[:-1]

    l = ""
    for i in no_stpwords_string.split(" "):
        l += snowball.stem(i) + " "

    return l[:-1]