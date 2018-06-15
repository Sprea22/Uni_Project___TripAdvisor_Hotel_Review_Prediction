import pandas as pd
from pgmpy.inference import VariableElimination
from Functions.Bayesian_Net_Model import Bayesian_Net_Model

# Read dataset already processed
# Create the BN Model and the Inference Model
# Test the performance on the first and second most probable values
# Report a file with the indexes of the "Strange" reviews

train = pd.read_csv("../Datasets/Final_Processed_Testing.csv")
#train = train.sample(2000)

test = pd.read_csv("../Datasets/Final_Processed_Testing.csv")
#test = test.sample(100)

true_label = test["Overall"]

train = train.drop(columns=["Unnamed: 0"])
test = test.drop(columns=["Unnamed: 0", "Overall"])

BN_Model = Bayesian_Net_Model(train)
inference_model = VariableElimination(BN_Model)

cols = test.columns.values

evidences_values = [None] * len(cols)
true_values = [None] * len(true_label)
pred_label1 = [None] * len(true_label)
pred_label2 = [None] * len(true_label)
cont = 0

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
    print(idx, true_label[idx])
    true_values[cont] = true_label[idx]
    pred_label1[cont] = first_max
    pred_label2[cont] = second_max
    cont = cont + 1

acc = 0.0
idx = []
for i in range(0, len(true_values)):
    if((pred_label1[i] == true_values[i]) or (pred_label2[i] == true_values[i])):
        acc += 1
    else:
        idx.append(i)
        print(true_values[i], pred_label1[i], pred_label2[i])
        print(test.iloc[i])
acc = acc / len(true_values)

print("Accuracy: ", acc)
print("Indexes of strange reviews", idx)
