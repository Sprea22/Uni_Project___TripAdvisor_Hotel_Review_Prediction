import numpy as np
import pandas as pd
import glob
import re

columns = ("Hotel_ID", "Overall Rating", "Avg. Price", "URL")
columns2 = ("Hotel_ID", "Author","Content","Date","No. Reader","No. Helpful","Overall","Value","Rooms","Location","Cleanliness","Check in / front desk","Service","Business service")

Testing_Dataset = pd.DataFrame( columns=columns2)
Training_Dataset = pd.DataFrame( columns=columns2)
Full_Dataset_CSV = pd.DataFrame( columns=columns2)

# Decomment if you want to integrate all the training & testing CSV files in two unique CSV files

for filename in glob.glob("Generated_Datasets/Testing_CSV/*.csv"):
    temp_file = pd.read_csv(filename)
    Testing_Dataset = Testing_Dataset.append(temp_file)
    temp_file = pd.read_csv(filename)
    Testing_Dataset = Testing_Dataset.append(temp_file)

Testing_Dataset.to_csv(path_or_buf = 'Testing_Dataset_FINAL.csv', columns = columns2, index = False)

for filename in glob.glob("Generated_Datasets/Training_CSV/*.csv"):
    temp_file = pd.read_csv(filename)
    Training_Dataset = Training_Dataset.append(temp_file)

Training_Dataset.to_csv(path_or_buf = 'Training_Dataset_FINAL.csv', columns = columns2, index = False)


# Decomment if you want to merge to different dataframes

Training_CSV = pd.read_csv("Generated_Datasets/Hotel_CSV/Hotel_Dataset_Training.csv")
Testing_CSV = pd.read_csv("Generated_Datasets/Hotel_CSV/Hotel_Dataset_Testing.csv")

Full_Dataset_CSV = Training_CSV.append(Testing_CSV)

Full_Dataset_CSV.loc[Full_Dataset_CSV['Avg. Price'].str.contains("<Avg. Price>"),'Avg. Price'] = "-1\r\n"

Full_Dataset_CSV['Avg. Price'] = Full_Dataset_CSV['Avg. Price'].replace('\r\n','', regex=True)

Full_Dataset_CSV['Avg. Price'] = Full_Dataset_CSV['Avg. Price'].replace(',','', regex=True)


Full_Dataset_CSV.to_csv(path_or_buf = 'Hotel_Full_Dataset_FINAL.csv', columns = columns, index = False)
