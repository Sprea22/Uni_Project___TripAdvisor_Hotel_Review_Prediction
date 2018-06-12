import numpy as np
import pandas as pd
import itertools
import nltk
from nltk import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from senticnet.senticnet import SenticNet
################################# TODO ###########################################

# Non ha senso farsi ritornare la stringa per poi ri tokenizzarla

# Vedere se i termini così hanno senso

# Ricreare il db con
     #solo ASCII
     #n* max di null

##################################################################################

def Terms_Chooser(data, n_of_words, polarity_threshold):
    sn = SenticNet()

    #choosing words
    data["Content"] = data["Content"].apply(lambda row: nltk.word_tokenize(row))

    lista = np.array(data["Content"].values.tolist())
    lista = list(itertools.chain.from_iterable(lista))

    FD = FreqDist(lista)
    MC = FD.most_common(n_of_words)

    common_words = []
    for i in range (0,n_of_words):
        common_words.append(MC[i][0])

    polarity = list()
    words = list()

    for x in common_words:
        try:
            temp = sn.polarity_intense(x)
            if (float(temp) > polarity_threshold or float(temp) < -(polarity_threshold)):
                polarity.append(temp)
                words.append(x)
        except Exception:
            continue

    return words
