import csv
import numpy as np
import pandas as pd

def deleteColumns(dataset, toDeleteColumns):
    print(dataset.dtypes)
    dataset = dataset.drop(columns=toDeleteColumns)
    print(dataset.dtypes)
    return dataset

Df_Train = pd.read_csv("../Datasets/Training.csv")
Df_Test = pd.read_csv("../Datasets/Testing.csv")
Df_Total = pd.read_csv("../Datasets/Dataset_Total.csv")

toDeleteColumns = ["Unnamed: 0", "Date"]

Df_Train = deleteColumns(Df_Train, toDeleteColumns)
Df_Test = deleteColumns(Df_Test, toDeleteColumns)
Df_Total = deleteColumns(Df_Total, toDeleteColumns)

Df_Train.to_csv("Training_New.csv", sep=',', index = False)
Df_Test.to_csv("Testing_New.csv", sep=',', index = False)
Df_Total.to_csv("Dataset_Total_New.csv", sep=',', index = False)
