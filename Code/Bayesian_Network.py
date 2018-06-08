import pgmpy
import pandas as pd
import numpy as np
from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import NaiveBayes
from pgmpy.inference import VariableElimination

# External implemented Functions
from Functions.Compute_CPT import Compute_CPT
from Functions.Compute_CPT import Generate_CPTs
from Functions.Data_Content_Processing import content_Processing
from Functions.Data_Terms_Adding import addColumns
from Functions.Terms_Chooser import terms_Chooser

def get_edges(cols, root):
    edges = []
    for i in cols:
        if (i != root):
            edge = [root,i]
            edges.append(edge)
    return edges

#############################################################
##### STEP1: Select the dataset for the Bayesian models #####
#############################################################
data = pd.read_csv("../Datasets/Training.csv")
#############################################################
##### STEP2: Dataset's content column processing        #####
#############################################################
# data["Content"] = content_Processing(data["Content"])

###############################################################
##### STEP3: Select which terms (boolean) you want to add #####
###############################################################
#Terms_to_add = terms_Chooser(data, 20)
Terms_to_add = ["good"]
data = addColumns(data, Terms_to_add)

###############################################################
##### STEP4: Delete useless columns from the dataset      #####
###############################################################
data = data.drop(columns=["Hotel_ID", "Content"])

###############################################################
##### STEP5: - Initialize NaiveBayes model's structure    #####
#####        - Compute the CPTs                           #####
#####        - Add the CPTs to the model                  #####
###############################################################
cols = data.columns.values
n_cols = len(data.columns.values)

G = NaiveBayes()
G.add_nodes_from(cols)
G.add_edges_from(get_edges(cols, 'Overall'))

data_cpts = Compute_CPT(data, "Overall")
list = Generate_CPTs(data_cpts, data, cols, 'Overall')
test_list =[None] * len(list)

for i in list:
    G.add_cpds(i)

# IMPORTANTE: SISTEMARE INDEX DELLE RIGHE E DELLE COLONNE
# AD ESEMPIO DOVE METTE OVERALL_0 INTENDE OVERALL = 1
# OVERALL_1 INTENDE OVERALL = 2 E COSì VIA PER TUTTE LE VARIABILI

###############################################################
##### STEP6: Inference testing part                       #####
###############################################################
inference = VariableElimination(G)
test = inference.query(variables = ['Overall'], evidence = {"Cleanliness":2, "Value":3, "Business service":3,
                                                            "Check in / front desk":2, "Location":4, "Rooms":3})
#print(test['Overall'])
test2 = inference.map_query(variables = ['Overall'], evidence = {"Cleanliness":5, "Value":5, "Business service":5,
                                                                "Check in / front desk":5, "Location":5, "Rooms":5})
#print(test2['Overall']+1)

###############################################################
##### STEP7: Inferences accuracy                          #####
###############################################################
testing_data = pd.read_csv("../Datasets/Testing.csv")

testing_data = testing_data[1:1000]
overall_test_data = testing_data["Overall"]

# testing_data["Content"] = content_Processing(testing_data["Content"])
#Terms_to_add = terms_Chooser(data, 20)
testing_data = addColumns(testing_data, Terms_to_add)
evidences_test_data = testing_data.drop(columns=["Hotel_ID", "Content", "Overall"])
cols = evidences_test_data.columns.values
evidences_values = [None] * len(cols)

cont_correct = 0
cont_error = 0
# Ordine: Value, rooms, location, cleanliness, check in/ front desk, service, business service
for (idx, row) in evidences_test_data.iterrows():
    if(row["Value"]!=-1 and row["Rooms"]!=-1 and row["Location"]!=-1 and row["Cleanliness"]!=-1 and row["Rooms"]!=-1):
        evidences_values = {}
        for i in cols:
            evidences_values[i] = row[i]
        pred_temp = inference.map_query(variables = ['Overall'], evidence = evidences_values)
        pred = pred_temp['Overall']+1
        #print("REAL: ", overall_test_data[idx], " -----> PRED:", pred['Overall']+1)
        if(pred == overall_test_data[idx]):
            cont_correct = cont_correct + 1
        else:
            cont_error = cont_error + 1

accuracy = cont_correct/(cont_correct+cont_error)
print("\n\n ACCURACY RESULT: ", accuracy, "\n\n")
