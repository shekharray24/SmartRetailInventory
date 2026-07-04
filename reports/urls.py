from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.reports_home,
        name="reports"
    ),

    path(
        "sales/pdf/",
        views.sales_pdf,
        name="sales_pdf"
    ),

    path(
        "inventory/excel/",
        views.inventory_excel,
        name="inventory_excel"
    ),

    path(
    "ai/pdf/",
    views.ai_report_pdf,
    name="ai_report_pdf"
    ),
]