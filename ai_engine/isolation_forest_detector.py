import numpy as np
from sklearn.ensemble import IsolationForest


def isolation_forest_detection(values):

    if len(values) < 5:
        return []

    data = np.array(values).reshape(-1, 1)

    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    predictions = model.fit_predict(data)

    anomalies = []

    for index, prediction in enumerate(predictions):

        if prediction == -1:

            anomalies.append(index)

    return anomalies