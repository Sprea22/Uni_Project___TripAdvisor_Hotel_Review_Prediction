import pgmpy
from Functions.Compute_CPT import Compute_CPT
from Functions.Compute_CPT import Generate_CPTs
from pgmpy.models import NaiveBayes
from pgmpy.factors.discrete import TabularCPD

def Bayesian_Net_Model(data):
    cols = data.columns.values
    n_cols = len(data.columns.values)

    BN_Model = NaiveBayes()
    BN_Model.add_nodes_from(cols)

    edges = []
    for i in cols:
        if (i != "Overall"):
            edge = ["Overall",i]
            edges.append(edge)

    BN_Model.add_edges_from(edges)

    print("Aggiunti Archi e Nodi \n\n")

    data_cpts = Compute_CPT(data, "Overall")
    CPTS_list = Generate_CPTs(data_cpts, data, cols, 'Overall')
    test_list =[None] * len(CPTS_list)

    for i in CPTS_list:
        BN_Model.add_cpds(i)

    print("Aggiunte CPD \n\n")

    return BN_Model
