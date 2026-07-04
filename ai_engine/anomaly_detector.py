import numpy as np


def z_score_detection(values, threshold=2):

    values = np.array(values)

    mean = np.mean(values)

    std = np.std(values)

    if std == 0:
        return []

    z_scores = (values - mean) / std

    anomalies = []

    for index, score in enumerate(z_scores):

        if abs(score) > threshold:

            anomalies.append(index)

    return anomalies