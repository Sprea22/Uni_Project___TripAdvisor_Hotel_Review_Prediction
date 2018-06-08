import csv
import numpy as np
import pandas as pd

def addColumns(dataset, Terms_to_add):
    for term in Terms_to_add:
        BoolColumn = []
        BoolColumn = dataset["Content"].apply(lambda row: int(term in row))
        columnName = "T:"+term
        dataset[columnName] = BoolColumn
    return dataset


Df_Train = pd.read_csv("../Datasets/Training.csv")
Terms_to_add = ["good", "normal", "bad"]

addColumns(Df_Train, Terms_to_add )

'''
Df_Train.to_csv("Training_New.csv", sep=',', index = False)
Df_Test.to_csv("Testing_New.csv", sep=',', index = False)
Df_Total.to_csv("Dataset_Total_New.csv", sep=',', index = False)
'''
