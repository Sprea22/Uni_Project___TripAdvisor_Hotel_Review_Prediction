import re
import glob
import numpy as np
import pandas as pd

def saveDataToExcel(name, content):
    writer = pd.ExcelWriter(name, engine="xlsxwriter")
    content.to_excel(writer, sheet_name='Sheet1')
    writer.save()

Dataset_Reviews = pd.read_csv("../Datasets/Dataset_Total.csv")
Dataset_Hotels = pd.read_csv("../Datasets/Hotels.csv")

# Number of reviewed hotels
N_Hotels = Dataset_Reviews['Hotel_ID'].nunique()
print("Number of reviewed hotels: ", N_Hotels, "\n")

# Number of reviews
N_Reviews = Dataset_Reviews['Hotel_ID'].count()
print("Number of reviews: ", N_Reviews, "\n")

# Group of hotels by rating
N_Hotels_Rating = Dataset_Hotels.groupby(['Overall Rating']).count()
print("Number of hotels grouped by rating: \n\n", N_Hotels_Rating[['Hotel_ID']], "\n")

# Group reviews by rating
N_Reviews_Rating= Dataset_Reviews.groupby(['Overall']).count()
print("Number of reviews grouped by rating: \n\n", N_Reviews_Rating[['Hotel_ID']], "\n")


print("####### Group By Average Price #######")
def groupByAvgPrice( int1, int2 ):
    print(int1, " - ", int2)
    print(Dataset_Hotels[(Dataset_Hotels["Avg. Price"] > int1) & (Dataset_Hotels["Avg. Price"]<= int2)]["Avg. Price"].count())

groupByAvgPrice(0, 100)
groupByAvgPrice(100, 200)
groupByAvgPrice(200, 300)
groupByAvgPrice(300, 400)
groupByAvgPrice(400, 500)
groupByAvgPrice(500, 10000)


# AVG PRICE ---> MIN: 100 MAX: 1142
#
# UNA BUONA IDEAA POTREBBE ESSERE NORMALIZZARE I VALORI IN BASE AL MINIMO ED AL MASSIMO
# CHAR --->     MIN: 8 MAX: 42170
# WORDS --->    MIN: 1 MAX: 7221
'''
# Number of char and words per text review
Dataset_Reviews['Chars Count'] = Dataset_Reviews['Content'].str.len()
Dataset_Reviews['Words Count']  = Dataset_Reviews['Content'].str.split().str.len()
Dataset_Reviews[["Chars Count","Words Count"]]

saveDataToExcel("Chars_Overall.xlsx", Dataset_Reviews[['Chars Count', "Overall"]])
saveDataToExcel("Words_Overall.xlsx", Dataset_Reviews[['Words Count', "Overall"]])
'''
'''
#  The "chars_COMPARED_rating" function counts how many reviews have a number of
# characters within the interval (int1, int2), and provides also the % compared with the total number of reviews and the mean overall rating
def chars_COMPARED_rating( int1, int2 ):
    count_chars = Dataset_Reviews[(Dataset_Reviews["Chars Count"] > int1) & (Dataset_Reviews["Chars Count"]<= int2)]["Chars Count"].count()
    print("Number of reviews with number of characters within (", int1, " and ", int2, "):", count_chars, ", that is the ", (count_chars/N_Reviews)*100, "% of the total reviews",
    "---> with a mean Overall rating of the reviews of:", Dataset_Reviews[(Dataset_Reviews["Chars Count"] > int1) & (Dataset_Reviews["Chars Count"]<= int2)]["Overall"].mean() )

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
    count_words = Dataset_Reviews[(Dataset_Reviews["Words Count"] > int1) & (Dataset_Reviews["Words Count"]<= int2)]["Words Count"].count()
    print("Number of reviews with number of words within (", int1, " and ", int2, "):" ,count_words, ", that is the ", (count_words/N_Reviews)*100, "% of the total reviews",
    "---> with a mean Overall rating of the reviews of:", Dataset_Reviews[(Dataset_Reviews["Words Count"] > int1) & (Dataset_Reviews["Words Count"]<= int2)]["Overall"].mean() )

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
'''
