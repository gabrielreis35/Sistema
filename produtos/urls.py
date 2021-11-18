from django.contrib import admin
from django.core.files.base import File
from django.urls import path
from . import views
from . import models

app_name = 'products'

urlpatterns = [
    path('', views.Products, name = 'Home_Products'),
    path('product/<int:id>', views.ViewProduct, name = 'View_Product'),
    path("addAll/", views.AddAllProduct, name="Add_All_Products"),
    path("UpdateAll/", views.UpdateAllProduct, name="Update_All_Product"),
    path('newProduct/', views.NewProduct, name = 'New_Products'),
    
    path("newSegment/", views.NewSegment, name="New_Segment"),
    path("newProductTip/", views.NewProductTip, name="New_Product_Tip"),
    path("newCategory/", views.NewCategory, name="New_Category"),
    path("newClass/", views.NewClass, name="New_Class"),
    
    path('viewSegment/', views.ViewSegment, name = 'View_Segment_Products'),
    path('viewProductTip/', views.ViewProductTip, name = 'View_ProductTip_Products'),
    path('viewCategory/', views.ViewCategory, name = 'View_Category_Products'),
    path('viewClass/', views.ViewClass, name = 'View_Class_Products'),
    
    path('updateSegment/<int:id>', views.UpdateSegment, name = 'Update_Segment_Products'),
    path('updateProductTip/<int:id>', views.UpdateProductTip, name = 'Update_ProductTip_Products'),
    path('updateCategory/<int:id>', views.UpdateCategory, name = 'Update_Category_Products'),
    path('updateClass/<int:id>', views.UpdateClass, name = 'Update_Class_Products'),
    
    path('update/<int:id>', views.UpdateProduct, name = 'Update_Product'),
    path('delete/<int:id>', views.DeleteProduct, name = 'Delete_Product'),
    path('newitem', views.NewItem, name = 'New_Item'),
    # path('downloaditem/<int:id>', views.DownloadItem, name = 'Download_Item'),
    path('deleteitem/<int:id>', views.DeleteItem, name = 'Delete_Item'),
    path('newfile', views.NewFile, name = 'New_File'),
    path('deletefile/<int:id>', views.DeleteFile, name = 'Delete_file'),
    
    path('serialNumber/', views.SerialNumber, name = 'Serial_Number'),
    path('newSerialNumber/', views.GenerateSerial, name = 'Generate_SerialNumber'),
    path("serialNumberid/<int:id>", views.GenerateSerialSingle , name="Generate_Single_SerialNumber")    
]
