import numpy as np
import pandas as pd
import glob
import re

Full_Dataset_Reviews = pd.read_csv("FINAl_Datasets/Full_Dataset_Reviews.csv")
Full_Dataset_Hotels = pd.read_csv("FINAl_Datasets/Hotel_Full_Dataset_FINAL.csv")

# Ner of reviewed hotels
N_Hotels = Full_Dataset_Reviews['Hotel_ID'].nunique()
print("Number of reviewd hotels: ", N_Hotels, "\n")

# Ner of reviews
N_Reviews = Full_Dataset_Reviews['Hotel_ID'].count()
print("Number of reviews: ", N_Reviews, "\n")

# Group of hotels by rating
N_Hotels_Rating = Full_Dataset_Hotels.groupby(['Overall Rating']).count()
print("Number of hotels grouped by rating: \n\n", N_Hotels_Rating[['Hotel_ID']], "\n")

# Group reviews by rating
N_Reviews_Rating= Full_Dataset_Reviews.groupby(['Overall']).count()
print("Number of reviews grouped by rating: \n\n", N_Reviews_Rating[['Hotel_ID']], "\n")

# Group of hotels by avg. price inteval  (0-150 , 151-300, 301-450, 451-600, 600-)
Hotels_Int_Unknown = Full_Dataset_Hotels[(Full_Dataset_Hotels["Avg. Price"] == -1)]["Avg. Price"].count()
Hotels_Int_0_100 = Full_Dataset_Hotels[(Full_Dataset_Hotels["Avg. Price"] > 0) & (Full_Dataset_Hotels["Avg. Price"]<= 100)]["Avg. Price"].count()
Hotels_Int_101_150 = Full_Dataset_Hotels[(Full_Dataset_Hotels["Avg. Price"] > 100) & (Full_Dataset_Hotels["Avg. Price"]<= 150)]["Avg. Price"].count()
Hotels_Int_151_200 = Full_Dataset_Hotels[(Full_Dataset_Hotels["Avg. Price"] > 150) & (Full_Dataset_Hotels["Avg. Price"]<= 200)]["Avg. Price"].count()
Hotels_Int_201_250 = Full_Dataset_Hotels[(Full_Dataset_Hotels["Avg. Price"] > 200) & (Full_Dataset_Hotels["Avg. Price"]<= 250)]["Avg. Price"].count()
Hotels_Int_251_300 = Full_Dataset_Hotels[(Full_Dataset_Hotels["Avg. Price"] > 250) & (Full_Dataset_Hotels["Avg. Price"]<= 300)]["Avg. Price"].count()
Hotels_Int_300_500 = Full_Dataset_Hotels[(Full_Dataset_Hotels["Avg. Price"] > 300) & (Full_Dataset_Hotels["Avg. Price"]<= 500)]["Avg. Price"].count()
Hotels_Int_501_inf = Full_Dataset_Hotels[(Full_Dataset_Hotels["Avg. Price"] > 500)]["Avg. Price"].count()

print("Number of hotels with avg. price Unknown :                   ", Hotels_Int_Unknown, "\n")
print("Number of hotels with avg. price <= 100 :                    ", Hotels_Int_0_100 , "\n")
print("Number of hotels with avg. price in range (101 : 150) :      ", Hotels_Int_101_150 , "\n")
print("Number of hotels with avg. price in range (151 : 200) :      ", Hotels_Int_151_200 , "\n")
print("Number of hotels with avg. price in range (201 : 250) :      ", Hotels_Int_201_250 , "\n")
print("Number of hotels with avg. price in range (251 : 300) :      ", Hotels_Int_251_300 , "\n")
print("Number of hotels with avg. price in range (300 : 500) :      ", Hotels_Int_300_500 , "\n")
print("Number of hotels with avg. price > 500 :                     ", Hotels_Int_501_inf , "\n")

# AVG PRICE ---> MIN: 100 MAX: 1142
#
# UNA BUONA IDEAA POTREBBE ESSERE NORMALIZZARE I VALORI IN BASE AL MINIMO ED AL MASSIMO
# CHAR --->     MIN: 8 MAX: 42170
# WORDS --->    MIN: 1 MAX: 7221

# Number of char and words per text review
Full_Dataset_Reviews['Chars Count'] = Full_Dataset_Reviews['Content'].str.len()
Full_Dataset_Reviews['Words Count']  = Full_Dataset_Reviews['Content'].str.split().str.len()
Full_Dataset_Reviews[["Chars Count","Words Count"]]

#  The "chars_COMPARED_rating" function counts how many reviews have a number of
# characters within the interval (int1, int2), and provides also the % compared with the total number of reviews and the mean overall rating
def chars_COMPARED_rating( int1, int2 ):
    count_chars = Full_Dataset_Reviews[(Full_Dataset_Reviews["Chars Count"] > int1) & (Full_Dataset_Reviews["Chars Count"]<= int2)]["Chars Count"].count()
    print("Number of reviews with number of characters within (", int1, " and ", int2, "):", count_chars, ", that is the ", (count_chars/N_Reviews)*100, "% of the total reviews",
    "---> with a mean Overall rating of the reviews of:", Full_Dataset_Reviews[(Full_Dataset_Reviews["Chars Count"] > int1) & (Full_Dataset_Reviews["Chars Count"]<= int2)]["Overall"].mean() )

chars_COMPARED_rating(0,500)
chars_COMPARED_rating(500,1000)
chars_COMPARED_rating(1000,1500)
chars_COMPARED_rating(1500,2500)
chars_COMPARED_rating(2500,3000)
chars_COMPARED_rating(3500, 4000)
chars_COMPARED_rating(4000,4500)
chars_COMPARED_rating(4500,5000)
chars_COMPARED_rating(5000,10000)
chars_COMPARED_rating(10000,20000)
chars_COMPARED_rating(20000,45000)

print("\n\n")

#  The "words_COMPARED_rating" function counts how many reviews have a number of
# words within the interval (int1, int2), and provides also the % compared with the total number of reviews and the mean overall rating
def words_COMPARED_rating( int1, int2 ):
    count_words = Full_Dataset_Reviews[(Full_Dataset_Reviews["Words Count"] > int1) & (Full_Dataset_Reviews["Words Count"]<= int2)]["Words Count"].count()
    print("Number of reviews with number of words within (", int1, " and ", int2, "):" ,count_words, ", that is the ", (count_words/N_Reviews)*100, "% of the total reviews",
    "---> with a mean Overall rating of the reviews of:", Full_Dataset_Reviews[(Full_Dataset_Reviews["Words Count"] > int1) & (Full_Dataset_Reviews["Words Count"]<= int2)]["Overall"].mean() )

words_COMPARED_rating(0,100)
words_COMPARED_rating(100,200)
words_COMPARED_rating(200,300)
words_COMPARED_rating(300,400)
words_COMPARED_rating(400,500)
words_COMPARED_rating(500, 600)
words_COMPARED_rating(600,700)
words_COMPARED_rating(700,1000)
words_COMPARED_rating(1000,3000)
words_COMPARED_rating(3000,5000)
words_COMPARED_rating(5000,7000)
