from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('suppliersapi/',views.Suppliers_Api.as_view()),
    path('customersapi/',views.Customers_Api.as_view()),
]