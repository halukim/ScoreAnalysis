from django.urls import path
from . import views

app_name = "analysis"

urlpatterns = [
    path('chart', views.ChartView.as_view(), name='chart'),
]