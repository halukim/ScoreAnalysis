from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path('list', views.ListView.as_view(), name='list'),
    path('', views.IndexView.as_view(), name='index'),
]
