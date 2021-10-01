from collections import namedtuple
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Products, name = 'Products'),
    path('product/<int:id>', views.ViewProduct, name = 'View_Product'),
    path('newproduct', views.NewProduct, name = 'New_Products'),
    path('update/<int:id>', views.UpdateProduct, name = 'Update_Product'),
    path('delete/<int:id>', views.DeleteProduct, name = 'Delete_Product'),
    path('newitem', views.NewItem, name = 'New_Item'),
    # path('downloaditem/<int:id>', views.DownloadItem, name = 'Download_Item'),
    path('deleteitem/<int:id>', views.DeleteItem, name = 'Delete_Item'),
    path('newfile', views.NewFile, name = 'New_File'),
    path('deletefile/<int:id>', views.DeleteFile, name = 'Delete_file'),
]
