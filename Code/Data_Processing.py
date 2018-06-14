import numpy as np
import pandas as pd
# External implemented Functions
from Functions.Data_Preprocessing import data_Preprocessing
from Functions.Data_Terms_Adding import addColumns

#############################################################
##### STEP1: Select the dataset for the Bayesian models #####
#############################################################
data = pd.read_csv("../Datasets/Reviews_Train.csv")
#data = data.sample(2000)

data_test = pd.read_csv("../Datasets/Reviews_Test.csv")
#data_test = data_test.sample(100)

Selected_Words = pd.read_csv("Words&Polarity_Choosen.csv")

print("Dataset Caricato \n\n")
###############################################################
##### STEP2: Data preprocessing                           #####
###############################################################
data, data_test = data_Preprocessing(data, data_test, 500, 0.8)

Selected_Words = pd.read_csv("../Datasets/Words&Polarity_Choosen.csv")

# Add the selected words to the dataframe (boolean)
data = addColumns(data, Selected_Words.T.values[0])
data_test = addColumns(data_test, Selected_Words.T.values[0])

# Drop the columns that are not needed
data = data.drop(columns=["Hotel_ID", "Content", "Unnamed: 0"])
data_test = data_test.drop(columns=["Hotel_ID", "Content", "Unnamed: 0"])

print("Final Dataframe Created\n\n")

# Decomment if you want to regenerate the processed dataset
#data.to_csv("Final_Processed_Training.csv", sep=",")
#data_test.to_csv("Final_Processed_Testing.csv", sep=",")
