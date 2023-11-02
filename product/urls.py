from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('addproduct/',views.AddProduct_Api.as_view()),
    path('addbrand/',views.Brand_Api.as_view()),
    path('addcategory/',views.Category_Api.as_view()),
    path('addwarranty/',views.Warranty_Api.as_view()),
    path('addunit/',views.Unit_Api.as_view()),
]