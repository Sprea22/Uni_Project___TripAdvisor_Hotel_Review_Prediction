import pgmpy
import pandas as pd
import numpy as np

from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import NaiveBayes
from pgmpy.inference import VariableElimination
from Compute_CPT import Compute_CPT

def get_edges(cols, root):
    edges = []
    for i in cols:
        if (i != root):
            edge = [root,i]
            edges.append(edge)
    return edges

def calculate_cpds(data_cpts, data, cols, root):
    cpts_list = []
    for i in cols:
        if (i == root):
            cpt = TabularCPD(
                                variable = root,
                                variable_card = 5,
                                values = [data_cpts[0].T.values[1]])
            print(cpt)
            print(cpt[0])
            cpts_list.append(cpt)
        else:
            cpt = TabularCPD(
                                variable = i,
                                #variable_card = len(data_cpts[np.where(cols == "B")[0][0]]),
                                variable_card = 2,
                                values = data_cpts[np.where(cols == i)[0][0]+1].T.values,
                                evidence=[root],
                                evidence_card=[5])
            cpts_list.append(cpt)
    return cpts_list

'''
data = pd.DataFrame(data={  'A': [1, 0, 0, 0, 1, 0, 1, 0],
                            'B': [0, 0, 0, 1, 0, 1, 1, 1],
                            'C': [0, 0, 0, 0, 0, 0, 0, 1],
                            'D': [0, 0, 0, 0, 0, 0, 0, 1],
                            'Overall': [1, 2, 3, 3, 3, 4, 4, 5],})
'''
data = pd.read_csv("../Datasets/Training.csv")

cols = data.columns.values
n_cols = len(data.columns.values)

G = NaiveBayes()
G.add_nodes_from(cols)
G.add_edges_from(get_edges(cols, 'Overall'))

data = data.drop(columns=["Hotel_ID", "Content"])

data_cpts = Compute_CPT(data, "Overall")

list = calculate_cpds(data_cpts, data, cols, 'Overall')
for i in list:
    #print(i)
    G.add_cpds(i)

inference = VariableElimination(G)

test = inference.query(variables = ['Overall'], evidence = {"A":0, "B":0, "C":0, "D":0})
print(test['Overall'])

#G.add_cpds(list)

'''
Model = NaiveBayes([("Overall", "Rooms")])

CPD_Overall = TabularCPD(
                    variable = "Overall",
                    variable_card = 5,
                    values = [[.1, .3, .4, 0, .2]])

CPD_Rooms = TabularCPD('Rooms', 6,
                            [[0, 0, 0, 0, 0],   #Rooms = 0 dato Overall = 0
                            [0.1, 0.1, 0.1, 0.1, 0.1],
                            [0.3, 0.2, 0.1, 0.3, 0.3],
                            [0.2, 0.3, 0.4, 0.2, 0.2],
                            [0.2, 0.2, 0.2, 0.2, 0.2],
                            [0.2, 0.2, 0.2, 0.2, 0.2]
                            ],
                            evidence=['Overall'], evidence_card=[5])
print(CPD_Overall)
print(CPD_Rooms)

Model.add_cpds(CPD_Overall, CPD_Rooms)
Model.get_cpds()
inference = VariableElimination(Model)

test = inference.query(variables = ["Overall"], evidence = {"Rooms":0})
print(test["Overall"])

test = inference.query(variables = ["Rooms"], evidence = {"Overall":1})
print(test["Rooms"])
'''
