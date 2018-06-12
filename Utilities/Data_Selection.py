import re
import glob
import csv
import numpy as np
import pandas as pd

Full_Dataset_Hotels = pd.read_csv("../../Datasets/Original/Full Original/Full_Dataset_Hotel.csv")
Full_Dataset_Reviews = pd.read_csv("../../Datasets/Original/Full Original/Full_Dataset_Reviews.csv")
# Decomment if you want to regenerate the training, testing and hotels Datasets
# With a smaller number of reviews.

Full_Dataset_Reviews["Null_Counter"] = Full_Dataset_Reviews.isin({-1}).sum(1)

data = Full_Dataset_Reviews.loc[Full_Dataset_Reviews["Null_Counter"] < 4]

# Drop the columns from the dataset that are not needed
toDeleteColumns = ["Date", "Author", "No. Reader", "No. Helpful", "Null_Counter"]
data = data.drop(columns=toDeleteColumns)

# Grouping the full dataset by Overall rating (1,2,3,4,5)
gb = data.groupby(['Overall'])

# Splitting the grouped Reviews into 5 different dataframes
Df1, Df2, Df3, Df4, Df5 = [gb.get_group(x) for x in gb.groups]

# Number of reviews per each Overall Rating values
n = 6500

# Sampling N reviews from the Df1: it contains just the reviews with "Overall" = 1
Df1 = Df1.sample(n)
# Creating a Df1_train dataframe that contains a random 70% of the sampled N reviews
Df1_train = Df1.sample(round(n/100*70))
# Creating a Df1_test dataframe that contains the remaining 30% of the NON sampled N reviews
Df1_test = pd.concat([Df1,Df1_train]).drop_duplicates(keep=False)

Df2 = Df2.sample(n)
Df2_train = Df2.sample(round(n/100*70))
Df2_test = pd.concat([Df2,Df2_train]).drop_duplicates(keep=False)

Df3 = Df3.sample(n)
Df3_train = Df3.sample(round(n/100*70))
Df3_test = pd.concat([Df3,Df3_train]).drop_duplicates(keep=False)

Df4 = Df4.sample(n)
Df4_train = Df4.sample(round(n/100*70))
Df4_test = pd.concat([Df4,Df4_train]).drop_duplicates(keep=False)

Df5 = Df5.sample(n)
Df5_train = Df5.sample(round(n/100*70))
Df5_test = pd.concat([Df5,Df5_train]).drop_duplicates(keep=False)

# Once all the train sets have been generated, the following instruction allow to merge them
# into a unique Train dataframea called "Df_Train"
# The same happens for the "Df_Test"
Df_Train = pd.concat([Df1_train, Df2_train, Df3_train, Df4_train, Df5_train])
Df_Test = pd.concat([Df1_test, Df2_test, Df3_test, Df4_test, Df5_test])

# Concatenating the Training and Testing set in order to get the Total dataset
Reviews = pd.concat([Df_Train, Df_Test])
# Modify the dataset about the hotels, because all the reviews about a single Hotels
# could have been deleted, so it doesn't make sense to keep the Hotel into the Hotels dataset
Df_Bool = Full_Dataset_Hotels['Hotel_ID'].isin(Reviews['Hotel_ID'])
Df_Hotel = Full_Dataset_Hotels[Df_Bool]

print(Df_Hotel)
# Decomment if you want to save the datasets

'''
Df_Hotel.to_csv("Hotels.csv", sep=',')
Df_Train.to_csv("Training.csv", sep=',')
Df_Test.to_csv("Testing.csv", sep=',')
Reviews.to_csv("Dataset_TOT.csv", sep=',')
'''
