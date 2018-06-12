import pgmpy
import pandas as pd
import numpy as np
from pgmpy.inference import VariableElimination

# External implemented Functions
from Functions.Data_Preprocessing import data_Preprocessing
from Functions.Bayesian_Net_Model import Bayesian_Net_Model
from Functions.Performance_Evaluation import performance_Evaluation

#############################################################
##### STEP1: Select the dataset for the Bayesian models #####
#############################################################
data = pd.read_csv("../Datasets/Reviews_Train.csv")
#data = data.sample(1000)

data_test = pd.read_csv("../Datasets/Reviews_Test.csv")
#data_test = data_test.sample(10)

print("Dataset Caricato \n\n")
###############################################################
##### STEP2: Data preprocessing                           #####
###############################################################
data, data_test = data_Preprocessing(data, data_test, 500, 0.8)

print("Final Dataframe Created\n\n")

###############################################################
##### STEP3: - Initialize NaiveBayes model's structure    #####
#####        - Compute the CPTs                           #####
#####        - Add the CPTs to the model                  #####
###############################################################
BN_Model = Bayesian_Net_Model(data)

print("Bayesian Net Model Created \n \n")

# IMPORTANTE: SISTEMARE INDEX DELLE RIGHE E DELLE COLONNE
# AD ESEMPIO DOVE METTE OVERALL_0 INTENDE OVERALL = 1
# OVERALL_1 INTENDE OVERALL = 2 E COSì VIA PER TUTTE LE VARIABILI

###############################################################
##### STEP4: Performance evaluation                       #####
###############################################################

inference_model = VariableElimination(BN_Model)

data.to_csv("Dataframe_Training_Processato500.csv", sep=",")
data_test.to_csv("Dataframe_Testing_Processato500.csv", sep=",")

performance_Evaluation(data, data_test, inference_model)
