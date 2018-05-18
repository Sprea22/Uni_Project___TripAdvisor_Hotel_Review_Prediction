import pandas as pd
import numpy as np


#read csv
filename = "dataset.csv"
csv = pd.read_csv(filename, sep = ";")
print csv
print "\n\n\n"

#access a column
column = csv.loc[:,"id"]
# same to csv.id
print "print column id"
print column
print "\n\n\n"

#access a colum data if
ifcolumn = csv.loc[(csv.numero == 4) & (csv.numero < 999)]
print "print alla value if column numero = 4 AND numero < 999"
print ifcolumn
print "\n\n\n"

#replace values if (in column)
csv.numero = csv.numero.replace(4,-11111111)
print "print csv with numero = 4 replaced with numero = 999"
print csv
print "\n\n\n"

#count value if
#NB csv.id.loc, NOT only csv.loc
positive = csv.id.loc[csv.numero < 0].count()
print "count all negative numbers"
print positive
print "\n\n\n"

#subsetting dataset
startRow = 1
endRow = 3
startCol = "nome"
EndCol = "cognome"

subset = csv.loc[startRow:endRow,startCol:EndCol]
print "print a subset of db row -> 1 to 3, cols -> nome to cognome"
print subset
print "\n\n\n"
