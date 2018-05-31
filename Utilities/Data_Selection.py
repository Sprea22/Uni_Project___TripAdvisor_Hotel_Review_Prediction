import re
import glob
import csv
import numpy as np
import pandas as pd

Df_Train = pd.read_csv("../Datasets/Training.csv")
Df_Test = pd.read_csv("../Datasets/Testing.csv")
Full_Dataset_Hotels = pd.read_csv("../Datasets/Full_Dataset_Hotel.csv")

# Decomment if you want toregenerate the training, testing and hotels Datasets
# With a smaller number of reviews.
'''
gb = Full_Dataset_Reviews.groupby(['Overall'])

Df1, Df2, Df3, Df4, Df5 = [gb.get_group(x) for x in gb.groups]

n = 9000

Df1 = Df1.sample(n)
Df1_train = Df1.sample(round(n/100*70))
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

#### #### Debugging #### ####
#print(pd.concat([Df1_test,Df1_train]).drop_duplicates(keep=False).shape)

Df_Train = pd.concat([Df1_train, Df2_train, Df3_train, Df4_train, Df5_train])
Df_Test = pd.concat([Df1_test, Df2_test, Df3_test, Df4_test, Df5_test])

Df_Tot = pd.concat([Df_Train, Df_Test])
Df_Bool = Full_Dataset_Hotels['Hotel_ID'].isin(Df_Tot['Hotel_ID'])
Df_Hotel = Full_Dataset_Hotels[Df_Bool]

'''

# Decomment if you want to save the datasets
'''
Df_Hotel.to_csv("Hotels.csv", sep=',')
Df_Train.to_csv("Training.csv", sep=',')
Df_Test.to_csv("Testing.csv", sep=',')
Df_Tot.to_csv("Dataset_TOT.csv", sep=',')
'''
