import pgmpy
import pandas as pd
import numpy as np
from pgmpy.inference import VariableElimination
from Functions.Data_Terms_Adding import addColumns



def single_Inference(inference_model, input_metadata, real_value, input_content):
    print(input_content)
    # METADATA order: "Value", "Rooms", "Location", "Cleanliness", "Check in / front desk", "Service", "Business service"
    evidences = [input_content]+input_metadata

    # Create a dataframe with the input review to test
    test = pd.DataFrame(columns=["Content" ,"Value", "Rooms", "Location", "Cleanliness", "Check in / front desk", "Service", "Business service"])
    test.loc[0] = evidences

    # Add the boolean terms column to the input review dataframeself.
    # The selected words have to be the same of the "data" dataframe which has been used for train the models
    Selected_Words = pd.read_csv("../Datasets/Words&Polarity_Choosen.csv")
    # Add the selected words to the dataframe (boolean)
    test = addColumns(test, Selected_Words.T.values[0])

    # Evidence instance creation and inference on the model.
    test = test.drop(columns=["Content"])
    cols = test.columns.values
    evidences_values = [None] * len(cols)
    for (idx, row) in test.iterrows():
        evidences_values = {}
        for i in cols:
            evidences_values[i] = row[i]
    prob_table = inference_model.query(variables = ['Overall'], evidence = evidences_values)
    pred_prob = prob_table["Overall"].values

    first_max_prob = max(pred_prob)
    for i in range(0, len(pred_prob)):
        if (pred_prob[i] == first_max_prob):
            first_max = i + 1
            pred_prob[i] = 0

    second_max_prob = max(pred_prob)
    for i in range(0, len(pred_prob)):
        if (pred_prob[i] == second_max_prob):
            second_max = i + 1
            pred_prob[i] = 0

    inc_review = False
    if(not((real_value == first_max) or (real_value == second_max))):
        inc_review = True

    return first_max, first_max_prob, second_max, second_max_prob, inc_review
