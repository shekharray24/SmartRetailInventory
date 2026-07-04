from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from sales.models import Sale
from django.db.models import Sum
from datetime import datetime
from openpyxl import Workbook
from products.models import Product
from ai_engine.database_detector import detect_sales_anomalies

def reports_home(request):

    return render(
        request,
        "reports/reports.html"
    )


def sales_pdf(request):

    if request.user.groups.filter(name="Staff").exists():

        return render(
            request,
            "errors/403.html",
            status=403
        )
    response = HttpResponse(content_type="application/pdf")

    response["Content-Disposition"] = 'attachment; filename="sales_report.pdf"'

    doc = SimpleDocTemplate(response)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph("<b>Smart Retail Inventory</b>", styles["Title"])
    )

    elements.append(
        Paragraph("Sales Report", styles["Heading2"])
    )

    elements.append(
        Paragraph(
            f"Generated On: {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph("<br/><br/>", styles["Normal"])
    )

    data = [

        ["Product", "Quantity", "Amount"]

    ]

    sales = Sale.objects.all()

    for sale in sales:

        data.append([

            sale.product.name,

            str(sale.quantity),

            f"₹ {sale.amount}"

        ])

    total = Sale.objects.aggregate(
        total=Sum("amount")
    )["total"] or 0

    data.append(["", "", ""])

    data.append(["", "Total Revenue", f"₹ {total}"])

    table = Table(data)

    table.setStyle(

        TableStyle([

            ("BACKGROUND", (0,0), (-1,0), colors.darkblue),

            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("GRID", (0,0), (-1,-1), 1, colors.black),

            ("BACKGROUND", (0,1), (-1,-2), colors.beige),

            ("BACKGROUND", (1,-1), (-1,-1), colors.lightgrey),

            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

            ("ALIGN", (0,0), (-1,-1), "CENTER"),

            ("BOTTOMPADDING", (0,0), (-1,0), 10),

        ])

    )

    elements.append(table)

    doc.build(elements)

    return response


def inventory_excel(request):

    if request.user.groups.filter(name="Staff").exists():

        return render(
            request,
            "errors/403.html",
            status=403
        )

    workbook = Workbook()

    worksheet = workbook.active

    worksheet.title = "Inventory Report"

    worksheet.append([
        "Product ID",
        "Product Name",
        "Category",
        "Brand",
        "Price",
        "Stock"
    ])

    products = Product.objects.all()

    for product in products:

        worksheet.append([

            product.product_id,

            product.name,

            product.category,

            product.brand,

            product.price,

            product.stock

        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = 'attachment; filename="inventory_report.xlsx"'

    workbook.save(response)

    return response

def ai_report_pdf(request):

    if request.user.groups.filter(name="Staff").exists():

        return render(
            request,
            "errors/403.html",
            status=403
        )

    response = HttpResponse(content_type="application/pdf")

    response["Content-Disposition"] = 'attachment; filename="ai_anomaly_report.pdf"'

    doc = SimpleDocTemplate(response)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "<b>Smart Retail Inventory</b>",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            "AI Anomaly Report",
            styles["Heading2"]
        )
    )

    anomalies = detect_sales_anomalies()

    data = [

        [

            "Sale Index",

            "Sales Quantity",

            "Status"

        ]

    ]

    for item in anomalies:

        data.append([

            str(item["index"]),

            str(item["sale"]),

            "Anomaly"

        ])

    data.append(["", "", ""])

    data.append([

        "",

        "Total",

        str(len(anomalies))

    ])

    table = Table(data)

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.darkblue),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,1),(-1,-2),colors.beige),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

        ])

    )

    elements.append(table)

    doc.build(elements)

    return response