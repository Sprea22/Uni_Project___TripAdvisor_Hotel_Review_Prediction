import re
import nltk
import string
import itertools
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from senticnet.senticnet import SenticNet
from Functions.Data_Terms_Adding import addColumns

def data_Preprocessing(data, data_test, n_of_words, polarity_threshold):
    Reviews = data["Content"]
    #Check if all char are ASCII
    # If we need another method for Encode/Decode there is string.printable method
    for i in range(0, len(Reviews)):
        x = Reviews.iloc[i].encode('ascii', errors = 'ignore').decode()

    # Set all the content to lower case
    Reviews = Reviews.apply(lambda row: row.lower())

    # Add to the follow variable the characters that you want to delete
    chars_to_del = "["+string.punctuation+string.digits+"]"
    # Delete all the chars in "chars_to_del" from each row of the dataframe
    Reviews = Reviews.apply(lambda row: re.sub(chars_to_del, '', row))
    # Tokenize every single words of the data content
    Token_Reviews = Reviews.apply(lambda row: nltk.word_tokenize(row))

    # Generating the list "stop" of element TO BE REMOVED from the sentences (stopwords, numbers and punctuations)
    stop = stopwords.words("english")
    # Remove all the words in the variable "stop"
    Filtered_Review = Token_Reviews.apply(lambda row: [w for w in row if not w in stop])

    # Stemming the data's content
    # Stemming the Filtered sentence, some stemmed words:
    # http://snowball.tartarus.org/algorithms/english/stemmer.html
    ps = PorterStemmer()
    for idx in range(0,len(Filtered_Review)):
        Stemmed_Review_temp = []
        for word in Filtered_Review.iloc[i]:
            Stemmed_Review_temp.append(ps.stem(word))
        Filtered_Review.iloc[i] = Stemmed_Review_temp

    # Terms choosing: most common word
    sn = SenticNet()

    Filtered_Review_List = list(itertools.chain.from_iterable(Filtered_Review))
    Words_Frquency = FreqDist(Filtered_Review_List)
    Most_Common_Words_Frequency = Words_Frquency.most_common(n_of_words)

    Most_Common_Words = []
    for i in range (0,n_of_words):
        Most_Common_Words.append(Most_Common_Words_Frequency[i][0])

    Selected_Words = []
    # Terms polarity
    for word in Most_Common_Words:
        try:
            temp = sn.polarity_intense(word)
            if (float(temp) > polarity_threshold or float(temp) < -(polarity_threshold)):
                Selected_Words.append(word)
        except Exception:
            continue

    # Add the selected words to the dataframe (boolean)
    data = addColumns(data, Selected_Words)
    data_test = addColumns(data_test, Selected_Words)

    # Drop the columns that are not needed
    data = data.drop(columns=["Hotel_ID", "Content", "Unnamed: 0"])
    data_test = data_test.drop(columns=["Hotel_ID", "Content", "Unnamed: 0"])

    return data, data_test
