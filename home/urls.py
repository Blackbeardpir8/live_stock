from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.stockpicker, name = "stockpicker"),
    path('stocktracker/', views.stocktracker, name = "stocktracker"),

]
