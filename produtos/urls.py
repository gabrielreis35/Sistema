from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Produtos, name = 'Produtos'),
    path('produto-<int:id>', views.viewProduto, name = 'View_Produtos'),
    path('addproduto', views.addProduto, name = 'add_Produtos'),
]
