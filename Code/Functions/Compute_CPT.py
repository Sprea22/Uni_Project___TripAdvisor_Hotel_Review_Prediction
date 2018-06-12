import numpy as np
import pandas as pd
from pgmpy.factors.discrete import TabularCPD

def Generate_CPTs(data_cpts, data, cols, root):
    cpts_list = []
    for i in cols:
        if (i == root):
            cpt = TabularCPD(
                                variable = root,
                                variable_card = 5,
                                values = [data_cpts[0].T.values[1]])
            cpts_list.append(cpt)
        elif(i[:2] == "T:"):
            cpt = TabularCPD(
                                variable = i,
                                #variable_card = len(data_cpts[np.where(cols == "B")[0][0]]),
                                variable_card = 2,
                                values = data_cpts[np.where(cols == i)[0][0]].T.values,
                                evidence=[root],
                                evidence_card=[5])
            cpts_list.append(cpt)
        else:
            cpt = TabularCPD(
                                variable = i,
                                #variable_card = len(data_cpts[np.where(cols == "B")[0][0]]),
                                variable_card = 6,
                                values = data_cpts[np.where(cols == i)[0][0]].T.values,
                                evidence=[root],
                                evidence_card=[5])
            cpts_list.append(cpt)
    return cpts_list

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

def Compute_CPT(data, root):
    data = data.replace(-1, 0)

    r,c = data.shape
    index = np.unique(data[root])

    true = data.groupby(root)[root].count() / r
    false = 1 - true
    CPT = pd.DataFrame(data = {'1': true, '0': false});
    index = np.unique(data[root])
    CPT.index = index.T

    gb = data.groupby([root])
    df1, df2, df3, df4, df5= [gb.get_group(x) for x in gb.groups]
    dfs = [df1, df2, df3, df4, df5]

    CPTs = []
    CPTs.append(CPT)
    cols = data.loc[:, data.columns != root]
    for node in cols:
        CPT_node = pd.DataFrame()
        p_val_node = np.unique(data[node])
        #flag = False
        for df in dfs:
            x = df.groupby(node)[node].count()
            val_node = x.index.values
            CPT = [0] * len(p_val_node)
            for i in val_node:
                #if (i == -1):
                #    print("ESGHERE")
                #    CPT[len(p_val_node)-1] = x[i] / x.sum().astype(float)
                #    flag = True
                #else:
                CPT[i] = x[i] / x.sum().astype(float)

            CPT_node = CPT_node.append(pd.Series(np.array(CPT)), ignore_index = True)
        #if (flag):
        #    CPT_node.rename(columns = {len(p_val_node)-1:-1}, inplace = True)

        CPT_node.index = CPT_node.index.values + 1
        CPTs.append(CPT_node)
    return CPTs
