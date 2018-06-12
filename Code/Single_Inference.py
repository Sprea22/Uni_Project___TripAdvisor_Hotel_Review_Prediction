import pgmpy
import pandas as pd
import numpy as np
from pgmpy.inference import VariableElimination

from Functions.Data_Preprocessing import data_Preprocessing
from Functions.Bayesian_Net_Model import Bayesian_Net_Model
from Functions.Performance_Evaluation import performance_Evaluation
from Functions.Data_Terms_Adding import addColumns


def single_Inference(input_metadata, input_content):
    # METADATA order: "Value", "Rooms", "Location", "Cleanliness", "Check in / front desk", "Service", "Business service"
    evidences = [input_content]+input_metadata

    # Select the already processed datasets and train the BN & Inference models
    data = pd.read_csv("Preproccessed_Datasets/Dataframe_Testing_Processato.csv")
    data = data.drop(columns=["Unnamed: 0"])
    BN_Model = Bayesian_Net_Model(data)
    inference_model = VariableElimination(BN_Model)

    # Create a dataframe with the input review to test
    data_test = pd.DataFrame(columns=["Content" ,"Value", "Rooms", "Location", "Cleanliness", "Check in / front desk", "Service", "Business service"])
    data_test.loc[0] = evidences

    # Add the boolean terms column to the input review dataframeself.
    # The selected words have to be the same of the "data" dataframe which has been used for train the models
    Selected_Words = []
    for i in data.columns.values:
        if(i[0]=="T"):
            Selected_Words.append(i[2:])

    # Evidence instance creation and inference on the model.
    data_test = data_test.drop(columns=["Content"])
    cols = data_test.columns.values
    evidences_values = [None] * len(cols)
    for (idx, row) in data_test.iterrows():
        evidences_values = {}
        for i in cols:
            evidences_values[i] = row[i]
        pred = inference_model.map_query(variables = ['Overall'], evidence = evidences_values)

    return pred["Overall"]+1
