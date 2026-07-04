from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ai_engine.database_detector import detect_sales_anomalies
from ai_engine.database_isolation import detect_isolation_anomalies
from ai_engine.database_lof import detect_lof_anomalies


@login_required
def analytics_dashboard(request):

    if not (
        request.user.is_superuser
        or request.user.groups.filter(name="Admin").exists()
        or request.user.groups.filter(name="Manager").exists()
    ):

        return render(
            request,
            "errors/403.html",
            status=403
        )

    context = {

        "zscore": detect_sales_anomalies(),

        "isolation": detect_isolation_anomalies(),

        "lof": detect_lof_anomalies(),

    }

    return render(
        request,
        "analytics/analytics.html",
        context
    )