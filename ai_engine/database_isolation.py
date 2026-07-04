from sales.models import Sale
from ai_engine.predict import predict_anomalies


def detect_isolation_anomalies():

    sales = Sale.objects.select_related("product").all()

    if sales.count() < 5:
        return []

    data = []
    sale_objects = []

    for sale in sales:

        data.append([

            sale.quantity,

            sale.product.price,

            sale.amount,

            sale.sale_date.weekday()

        ])

        sale_objects.append(sale)

    predictions = predict_anomalies(data)

    anomalies = []

    for i, prediction in enumerate(predictions):

        if prediction == -1:

            anomalies.append({

                "index": i,

                "product": sale_objects[i].product.name,

                "sale": sale_objects[i].quantity,

                "amount": sale_objects[i].amount

            })

    return anomalies