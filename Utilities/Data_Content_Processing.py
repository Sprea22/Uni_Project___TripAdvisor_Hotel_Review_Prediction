import re
import nltk
import string
import numpy as np
import pandas as pd
import csv
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

def content_Processing(Reviews):
    #Check if all char are ASCII
    #for i in range(0, len(Reviews)):
    #    Reviews[i] = Reviews[i].encode('ascii', errors='ignore')

    # Generating the list "stop" of element TO BE REMOVED from the sentences
    stop = stopwords.words("english") + list(string.punctuation)

    # Delete all the numbers from the original "Content"
    #Reviews = pd.DataFrame(re.sub(r'\d+', '', text), index=range(1), columns=['A'])
    Reviews = Reviews.apply(lambda row: row.lower())

    Token_Reviews = Reviews.apply(lambda row: nltk.word_tokenize(row))

    Filtered_sentence = Token_Reviews.apply(lambda row: [w for w in row if not w in stop])

    # Stemming the Filtered sentence, some stemmed words:
    # http://snowball.tartarus.org/algorithms/english/stemmer.html
    Stemmed_sentence = pd.DataFrame(columns=["Content"])

    ps = PorterStemmer()
    for sentence in Filtered_sentence:
        Stemmed_sentence_temp = []
        for word in sentence:
            Stemmed_sentence_temp.append(ps.stem(word))

        Stemmed_sentence_temp = ' '.join(Stemmed_sentence_temp)
        Stemmed_sentence = Stemmed_sentence.append(pd.Series(np.array([Stemmed_sentence_temp])), ignore_index=True)
        #Stemmed_sentence = pd.DataFrame(Stemmed_sentence[1], columns=["Content"])
        #sno = nltk.stem.SnowballStemmer('english')
        #for word2 in sentence:
        #    Stemmed_sentence.append(sno.stem(word2))
    Stemmed_sentence["Content"] = Stemmed_sentence[0]
    return Stemmed_sentence["Content"]
