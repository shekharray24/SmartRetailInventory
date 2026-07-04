from sales.models import Sale
from ai_engine.anomaly_detector import z_score_detection


def detect_sales_anomalies():

    sales = list(
        Sale.objects.values_list(
            "quantity",
            flat=True
        )
    )

    if len(sales) < 5:
        return []

    anomaly_indexes = z_score_detection(sales)

    anomalies = []

    for index in anomaly_indexes:

        anomalies.append({

            "sale": sales[index],

            "index": index

        })

    return anomalies