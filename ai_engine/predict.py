import os
import joblib
import numpy as np


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -----------------------------
# Load trained model
# -----------------------------

model = joblib.load(
    os.path.join(
        BASE_DIR,
        "models",
        "isolation_forest.pkl"
    )
)

# -----------------------------
# Load scaler
# -----------------------------

scaler = joblib.load(
    os.path.join(
        BASE_DIR,
        "models",
        "scaler.pkl"
    )
)


# -----------------------------
# Prediction Function
# -----------------------------

def predict_anomalies(data):

    """
    data format:

    [
        [Quantity, UnitPrice, TotalAmount, DayOfWeek],
        ...
    ]
    """

    data = np.array(data)

    scaled_data = scaler.transform(data)

    predictions = model.predict(scaled_data)

    return predictions.tolist()