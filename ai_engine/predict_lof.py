import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

lof_model = joblib.load(
    os.path.join(
        BASE_DIR,
        "models",
        "lof.pkl"
    )
)

scaler = joblib.load(
    os.path.join(
        BASE_DIR,
        "models",
        "scaler.pkl"
    )
)


def predict_lof(data):

    data = np.array(data)

    data_scaled = scaler.transform(data)

    predictions = lof_model.predict(data_scaled)

    return predictions.tolist()