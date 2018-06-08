from nltk import FreqDist
import pandas as pd
import numpy as np
from Data_Content_Processing import content_Processing

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import itertools

'''
def terms_Chooser():
'''    
n_of_words = 20

data = pd.read_csv("../../Datasets/Training.csv")

dati_DIOCANE = data

dati_DIOCANE["Content"] = content_Processing(dati_DIOCANE["Content"])

dati_DIOCANE["Content"] = dati_DIOCANE["Content"].apply(lambda row: nltk.word_tokenize(row))

lista = np.array(dati_DIOCANE["Content"].values.tolist())

lista = list(itertools.chain.from_iterable(lista))

#print lista
FD = FreqDist(lista)
MC = FD.most_common(n_of_words)

res = []
for i in range (0,n_of_words):
    res.append(MC[i][0])

print(res)

'''
def terms_Chooser():
    n_of_words = 3

    data = pd.read_csv("../Datasets/Training.csv")

    #lista = np.array(data['Content'].values.tolist()).flatten()

    lista = np.array(data['Content'][0])

    #print lista
    FD = FreqDist(lista)
    MC = FD.most_common(n_of_words)

    res = []
    for i in range (0,n_of_words):
        res.append(MC[i][0])

    print(res)
'''
