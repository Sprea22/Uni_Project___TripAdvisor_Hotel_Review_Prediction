from sklearn.metrics import confusion_matrix
from sklearn.metrics import *
from sklearn.preprocessing import label_binarize
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def performance_Evaluation(data, data_test, inference_model):
    true_label = data_test["Overall"]
    pred_label = data_test["Overall"]
    data_test = data_test.drop(columns=["Overall"])
    cols = data_test.columns.values
    evidences_values = [None] * len(cols)

    true_values = [None] * len(true_label)
    cont = 0
    for (idx, row) in data_test.iterrows():
        evidences_values = {}
        for i in cols:
            evidences_values[i] = row[i]
        pred = inference_model.map_query(variables = ['Overall'], evidence = evidences_values)
        true_values[cont] = true_label[idx]
        cont = cont + 1
        pred_label[idx] = pred["Overall"]+1

    y_true = true_values
    y_pred = pred_label

    accuracy = accuracy_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred, average="weighted")
    precision = precision_score(y_true, y_pred, average="weighted")
    f1 = f1_score(y_true, y_pred, average='weighted')
    # Real on the Y axis, pred on the X axis

    print("Accuracy: ", accuracy)
    # Sul totale numero di istanze true con label = 0, quanti ne ha predetti correttamente a 0?
    # Number of 0 in y_pred AND y_true / Number of 0 in y_real
    print("Recall: ", recall)
    # Number of 0 in y_pred AND y_true / Number of 0 in y_pred
    # Sul totale numero di istanze predette con label = 0, quanti sono effettivamente a 0?
    print("Precision: ", precision)

    print("F1_score: ", f1)

    return ""
