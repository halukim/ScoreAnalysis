from django.urls import path
from . import views

app_name = "analysis"

urlpatterns = [
    path('fx/bitcoin', views.BitcoinView.as_view(), name='bitcoin'),
    path('fx/gold', views.BitcoinView.as_view(), name='gold'),
    path('list', views.BitcoinView.as_view(), name='list'),

    path('powerball', views.BitcoinView.as_view(), name='powerball'),
]
