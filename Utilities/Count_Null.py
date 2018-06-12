import pandas as pd

data = pd.read_csv("Full_Dataset_Reviews.csv")


#############################################
#  PROVO A DROPPARE LE COLONNE DEI LETTORI  #
#############################################
data = data.where(data!=-1, None)
data['Content'] = data.isnull().sum(axis=1)

gb = data.groupby('Content')
zero, one, two, three, four, five, six, seven, eight, nine =  [gb.get_group(x) for x in gb.groups]

dfs = [zero, one, two, three, four, five, six, seven, eight, nine]

c = 0
for df in dfs:
    print "dataframe con " + str(c) + " elementi nulli"
    c = c + 1;
    dfg = df.groupby('Overall')['Overall'].count()
    print dfg
    print "\n" + "N' totale di elementi " + str(dfg.sum())
    print "\n\n"

'''
zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0

for x in n_of_null:
    if (x == 0):
        zero = zero + 1
    elif (x == 1):
        one = one + 1
    elif (x == 2):
        two = two + 1
    elif (x == 3):
        three = three + 1
    elif (x == 4):
        four = four + 1
    elif (x == 5):
        five = five + 1
    elif (x == 6):
        six = six + 1
    elif (x == 7):
        seven = seven + 1
    elif (x == 8):
        eith = eight + 1
    elif (x == 9):
        nine = nine + 1
    elif (x == 10):
        ten = ten + 1

print "0 null values " + str(zero)
print "1 null values " + str(one)
print "2 null values " + str(two)
print "3 null values " + str(three)
print "4 null values " + str(four)
print "5 null values " + str(five)
print "6 null values " + str(six)
print "7 null values " + str(seven)
print "8 null values " + str(eight)
print "9 null values " + str(nine)
print "10 null values " + str(ten)
'''
