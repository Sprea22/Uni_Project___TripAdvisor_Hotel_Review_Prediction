import numpy as np
import pandas as pd
import nltk
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

Dataset_Reviews = pd.read_csv("../Datasets/Dataset_Total.csv")
Dataset_Hotels = pd.read_csv("../Datasets/Hotels.csv")

stop = stopwords.words("english") + list(string.punctuation)
#Reviews = Dataset_Reviews["Content"]

text = "me and 999999 MY FRIEND, Mirko are going. 11 to fuck! ourselves"
print(text)

Reviews = pd.DataFrame(re.sub(r'\d+', '', text), index=range(1), columns=['A'])

print(Reviews)

Reviews['A'] = Reviews['A'].str.lower()

Token_Reviews = Reviews.apply(lambda row: nltk.word_tokenize(row['A']), axis=1)

print(Token_Reviews)

Filtered_sentence = Token_Reviews.apply(lambda row: [w for w in row if not w in stop])

print(Filtered_sentence)
