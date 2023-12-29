from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StockFetcher, name = 'StockFetcher'),
    path('stocks/', views.StockTracker, name='StockTracker')
]