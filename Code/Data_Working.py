import csv
import numpy as np
import pandas as pd
from Data_Content_Processing import content_Processing
from Data_Terms_Adding import addColumns
from Compute_CPT import Compute_CPT
from Terms_Chooser import terms_Choice

Df_Train = pd.read_csv("../Datasets/Training.csv")

Df_Train["Content"] = content_Processing(Df_Train["Content"])

Terms_to_add = ["good", "normal", "bad"]

Df_Train = addColumns(Df_Train, terms_Choice())

Df_Train = Df_Train.drop(columns=["Hotel_ID", "Content"])

CPTs = Compute_CPT(Df_Train, "Overall")

for i in range(0,len(CPTs)):
    print(Df_Train.columns.values[i])
    print(CPTs[i], "\n")
