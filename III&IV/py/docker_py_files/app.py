from flask import Flask, request, jsonify
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import os
import numpy as np
import pickle

DATASET_PATH = os.environ.get('DATASET_PATH')
MODEL_PATH = os.environ.get('MODEL_PATH')
# DATASET_PATH = 'wine-quality-white-and-red.csv'
print("Initialized DATASET_PATH var: ", DATASET_PATH)
print("Initialized MODEL_PATH var: ", MODEL_PATH)

app = Flask(__name__)

model_trained = False
sc = StandardScaler()
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, 'rb') as f:
        mlp_clf, sc = pickle.load(f)
        model_trained = True
    print("Model is LOADED on initialization")
else:
    mlp_clf = MLPClassifier(hidden_layer_sizes=(150, 100, 50),
                            max_iter=300, activation='relu',
                            solver='adam')
    print("Model is CREATED on initialization")


def metrics_to_json(target_class, accuracy, precision, recall, f1_score, support):
    metrics = {}

    for i, c in enumerate(target_class):
        metrics[c] = {
            "precision": str(precision[i]),
            "recall": str(recall[i]),
            "f1-score": str(f1_score[i]),
            "support": str(support[i])
        }
    metrics["accuracy"] = str(accuracy)
    return jsonify(metrics)


@app.route("/train", methods=["POST"])
def train():
    global model_trained, sc
    test_size = request.json.get('test_size')

    df = pd.read_csv(DATASET_PATH)

    x = df.drop('type', axis=1)
    y = df['type']

    trainX, testX, trainY, testY = train_test_split(x, y, test_size=test_size)
    # test_size is 0.25 by default

    scaler = sc.fit(trainX)
    trainX_scaled = scaler.transform(trainX)
    testX_scaled = scaler.transform(testX)

    mlp_clf.fit(trainX_scaled, trainY)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump((mlp_clf, scaler), f)
    y_pred = mlp_clf.predict(testX_scaled)

    accuracy = accuracy_score(testY, y_pred)
    precision, recall, f1_score, support = precision_recall_fscore_support(
        testY, y_pred)

    model_trained = True

    return metrics_to_json(y.unique(), accuracy,
                           precision, recall, f1_score, support)


@app.route("/predict", methods=["POST"])
def predict():
    global model_trained, sc

    if model_trained is False:
        return jsonify({
            "message": "please trigger /train endpoint before using /predict"
        })

    data_to_predict = request.json.get('data')
    data_scaled = sc.transform(np.array(data_to_predict).reshape(1, -1))
    pred = mlp_clf.predict(data_scaled)
    return jsonify({"prediction": pred.tolist()})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
