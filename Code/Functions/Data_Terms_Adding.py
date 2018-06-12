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
