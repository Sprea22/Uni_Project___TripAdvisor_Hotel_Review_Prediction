import nltk
import itertools
import pandas as pd
import numpy as np
from nltk import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize

def terms_Chooser(data, n_of_words):
    data["Content"] = data["Content"].apply(lambda row: nltk.word_tokenize(row))
    lista = np.array(data["Content"].values.tolist())
    lista = list(itertools.chain.from_iterable(lista))

    FD = FreqDist(lista)
    MC = FD.most_common(n_of_words)

    res = []
    for i in range (0,n_of_words):
        res.append(MC[i][0])

    return (res)
