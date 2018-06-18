import numpy as np
import pandas as pd
import glob
import re

hotel_columns = ("Overall Rating", "Avg. Price", "URL")
hotel_columns2 = ("Hotel_ID", "Overall Rating", "Avg. Price", "URL")

columns = ("Author","Content","Date","No. Reader","No. Helpful","Overall","Value","Rooms","Location","Cleanliness","Check in / front desk","Service","Business service")
columns2 = ("Hotel_ID", "Author","Content","Date","No. Reader","No. Helpful","Overall","Value","Rooms","Location","Cleanliness","Check in / front desk","Service","Business service")

review_dataset = pd.DataFrame( columns=columns)
hotel_dataset = pd.DataFrame( columns = hotel_columns)
cont_removed = 0

for filename in glob.glob("Testing/*.dat"):
    Hotel_ID = re.findall('\d+', filename)

    with open(filename, encoding="utf8") as f:
        not_url_flag = 1
        temp_row_hotel = []
        head = [next(f) for x in range(4)]

        for word in head:
            if(word == "\n"):
                if(len(temp_row_hotel) == 3):
                    temp_row_hotel = pd.DataFrame([temp_row_hotel], columns = hotel_columns)
                    hotel_df = pd.DataFrame({'Hotel_ID': Hotel_ID})
                    temp_row_hotel = hotel_df.join(temp_row_hotel)
                    hotel_dataset = hotel_dataset.append(temp_row_hotel)
                    temp_row_hotel = []
                else:
                    not_url_flag = 0
                    #temp_row_hotel.append("Missing_URL")

            elif("<Overall Rating>" in word):
                word = word.replace("<Overall Rating>", "")
                temp_row_hotel.append(word)

            elif("<Avg. Price>" in word):
                word = word.replace("<Avg. Price>$", "")
                temp_row_hotel.append(word)

            elif("<URL>" in word):
                word = word.replace("<URL>", "")
                temp_row_hotel.append(word)
            else:
                not_url_flag = 0

        if(not_url_flag != 0):
            temp_row = []

            for word in f:
                if(word == "\n"):
                    temp_row = pd.DataFrame([temp_row], columns = columns)
                    if("showReview(" not in temp_row["Content"][0]):
                        hotel_df = pd.DataFrame({'Hotel_ID': Hotel_ID})
                        temp_row = hotel_df.join(temp_row)
                        review_dataset = review_dataset.append(temp_row)
                    temp_row = []

                elif("<Author>" in word):
                    word = word.replace("<Author>", "")
                    temp_row.append(word)

                elif("<Content>" in word):
                    word = word.replace("<Content>", "")
                    temp_row.append(word)

                elif("<Date>" in word):
                    word = word.replace("<Date>", "")
                    temp_row.append(word)

                elif("<No. Reader>" in word):
                    word = word.replace("<No. Reader>", "")
                    temp_row.append(word)

                elif("<No. Helpful>" in word):
                    word = word.replace("<No. Helpful>", "")
                    temp_row.append(word)

                elif("<Overall>" in word):
                    word = word.replace("<Overall>", "")
                    temp_row.append(word)

                elif("<Value>" in word):
                    word = word.replace("<Value>", "")
                    temp_row.append(word)

                elif("<Rooms>" in word):
                    word = word.replace("<Rooms>", "")
                    temp_row.append(word)

                elif("<Location>" in word):
                    word = word.replace("<Location>", "")
                    temp_row.append(word)

                elif("<Cleanliness>" in word):
                    word = word.replace("<Cleanliness>", "")
                    temp_row.append(word)

                elif("<Check in / front desk>" in word):
                    word = word.replace("<Check in / front desk>", "")
                    temp_row.append(word)

                elif("<Service>" in word):
                    word = word.replace("<Service>", "")
                    temp_row.append(word)

                elif("<Business service>" in word):
                    word = word.replace("<Business service>", "")
                    temp_row.append(word)

            review_dataset.to_csv(path_or_buf = 'Generated_Datasets/Training_CSV/Reviews_'+Hotel_ID[0]+'.csv', columns = columns2, index = False)
            review_dataset = pd.DataFrame( columns=columns)

        else:
            print("Esghere!")
            cont_removed = cont_removed + 1
            print(cont_removed)



hotel_dataset.to_csv(path_or_buf = 'Generated_Datasets/Hotel_CSV/Hotel_Dataset_Testing.csv', columns = hotel_columns2, index = False)
