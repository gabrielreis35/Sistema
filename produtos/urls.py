from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Products, name = 'Products'),
    path('product-<int:id>', views.ViewProduct, name = 'View_Products'),
    path('newproduct', views.NewProduct, name = 'New_Products'),
]
