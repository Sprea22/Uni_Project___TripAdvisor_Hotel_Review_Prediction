import re
import glob
import numpy as np
import pandas as pd

#### #### #### #### #### #### ####
####   FUNCTIONS AND UTILITY  ####
#### #### #### #### #### #### ####

# The "saveDataToExcel" function allows to save a dataframe in xlsx format
def saveDataToExcel(name, content):
    writer = pd.ExcelWriter(name, engine="xlsxwriter")
    content.to_excel(writer, sheet_name='Sheet1')
    writer.save()

# The "groupByAvgPrice" function counts how many hotels have an average price between "int1" and "int2"
def groupByAvgPrice( int1, int2 ):
    print("Number of hotels with AVG-price between", int1, " - ", int2, "---->", (Dataset_Hotels[(Dataset_Hotels["Avg. Price"] > int1) & (Dataset_Hotels["Avg. Price"]<= int2)]["Avg. Price"].count()))

#  The "words_COMPARED_rating" function counts how many reviews have a number of
# words within the interval (int1, int2), and provides also the % compared with the total number of reviews and the mean overall rating
def words_COMPARED_rating( int1, int2 ):
    count_words = Dataset_Reviews[(Dataset_Reviews["Words Count"] > int1) & (Dataset_Reviews["Words Count"]<= int2)]["Words Count"].count()
    print("Number of reviews with number of words within (", int1, " and ", int2, "):" ,count_words, ", that is the ", (count_words/N_Reviews)*100, "% of the total reviews",
    "---> with a mean Overall rating of the reviews of:", Dataset_Reviews[(Dataset_Reviews["Words Count"] > int1) & (Dataset_Reviews["Words Count"]<= int2)]["Overall"].mean() )

#  The "chars_COMPARED_rating" function counts how many reviews have a number of
# characters within the interval (int1, int2), and provides also the % compared with the total number of reviews and the mean overall rating
def chars_COMPARED_rating( int1, int2 ):
    count_chars = Dataset_Reviews[(Dataset_Reviews["Chars Count"] > int1) & (Dataset_Reviews["Chars Count"]<= int2)]["Chars Count"].count()
    print("Number of reviews with number of characters within (", int1, " and ", int2, "):", count_chars, ", that is the ", (count_chars/N_Reviews)*100, "% of the total reviews",
    "---> with a mean Overall rating of the reviews of:", Dataset_Reviews[(Dataset_Reviews["Chars Count"] > int1) & (Dataset_Reviews["Chars Count"]<= int2)]["Overall"].mean() )


def reviewsDatasetAnalysis(input_reviews_dataset):
    print("\n\n######## REVIEWS DATASET ANALYSIS ########\n\n")
    # Number of reviews
    N_Reviews = input_reviews_dataset['Hotel_ID'].count()
    print("Number of reviews: ", N_Reviews, "\n")
    # Group reviews by rating
    N_Reviews_Rating= input_reviews_dataset.groupby(['Overall']).count()
    print("Number of reviews grouped by rating: \n\n", N_Reviews_Rating[['Hotel_ID']], "\n")
    # Number of char and words per text review
    input_reviews_dataset['Chars Count'] = input_reviews_dataset['Content'].str.len()
    input_reviews_dataset['Words Count']  = input_reviews_dataset['Content'].str.split().str.len()
    input_reviews_dataset[["Chars Count","Words Count"]]
    # Number of null value per column
    print("### Not null values per each column ###")
    print((input_reviews_dataset !=-1).sum(), "\n")
    print("### NULL values per each column ###")
    print((input_reviews_dataset ==-1).sum())

    print("####################################################")

def hotelsDatasetAnalysis(input_hotels_dataset):
    print("\n\n######## HOTELS DATASET ANALYSIS ########\n\n")
    # Number of reviewed hotels
    N_Hotels = Dataset_Reviews['Hotel_ID'].nunique()
    print("Number of reviewed hotels: ", N_Hotels, "\n")
    # Group of hotels by rating
    N_Hotels_Rating = Dataset_Hotels.groupby(['Overall Rating']).count()
    print("Number of hotels grouped by rating: \n\n", N_Hotels_Rating[['Hotel_ID']], "\n")
    print("####### Group By Average Price #######")
    groupByAvgPrice(0, 100)
    groupByAvgPrice(100, 200)
    groupByAvgPrice(200, 300)
    groupByAvgPrice(300, 400)
    groupByAvgPrice(400, 500)
    groupByAvgPrice(500, 10000)

    print("####################################################")

#### #### #### #### #### #### #### #### #### #### #### #### #### ####
#### #### #### #### #### #### #### #### #### #### #### #### #### ####
#### #### #### #### #### #### #### #### #### #### #### #### #### ####


Dataset_Reviews = pd.read_csv("../Datasets/Dataset_Total.csv")
Dataset_Hotels = pd.read_csv("../Datasets/Hotels.csv")

reviewsDatasetAnalysis(Dataset_Reviews)
hotelsDatasetAnalysis(Dataset_Hotels)



'''

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
