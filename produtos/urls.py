from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.Products, name = 'Home_Products'),
    path('product/<int:id>', views.ViewProduct, name = 'View_Product'),
    
    path('newProduct/', views.NewProduct, name = 'New_Products'),
    path('newitem/<int:id>', views.NewItem, name = 'New_Item'),
    path('newfile/<int:id>', views.NewFile, name = 'New_File'),
    path("newSegment/", views.NewSegment, name="New_Segment"),
    path("newProductTip/", views.NewProductTip, name="New_Product_Tip"),
    path("newCategory/", views.NewCategory, name="New_Category"),
    path("newClass/", views.NewClass, name="New_Class"),
    
    path('viewSegment/', views.ViewSegment, name = 'View_Segment_Products'),
    path('viewProductTip/', views.ViewProductTip, name = 'View_ProductTip_Products'),
    path('viewCategory/', views.ViewCategory, name = 'View_Category_Products'),
    path('viewClass/', views.ViewClass, name = 'View_Class_Products'),
    
    path('update/<int:id>', views.UpdateProduct, name = 'Update_Product'),
    path('updateSegment/<int:id>', views.UpdateSegment, name = 'Update_Segment_Products'),
    path('updateProductTip/<int:id>', views.UpdateProductTip, name = 'Update_ProductTip_Products'),
    path('updateCategory/<int:id>', views.UpdateCategory, name = 'Update_Category_Products'),
    path('updateClass/<int:id>', views.UpdateClass, name = 'Update_Class_Products'),

    path('delete/<int:id>', views.DeleteProduct, name = 'Delete_Product'),
    path('deleteitem/<int:id>', views.DeleteItem, name = 'Delete_Item'),
    path('deletefile/<int:id>', views.DeleteFile, name = 'Delete_file'),
    path('deleteSegment/<int:id>', views.DeleteSegment, name = 'Delete_Segment_Product'),
    path('deleteProductTip/<int:id>', views.DeleteProductTip, name = 'Delete_ProductTip_Product'),
    path('deleteCategory/<int:id>', views.DeleteCategory, name = 'Delete_Category_Product'),
    path('deleteClassProduct/<int:id>', views.DeleteClassProduct, name = 'Delete_Class_Product'),

    path('downloaditem/<int:id>', views.DownloadItem, name = 'Download_Item'),

    path('serialNumber/', views.SerialNumber, name = 'Serial_Number'),
    path('newSerialNumber/', views.GenerateSerial, name = 'Generate_SerialNumber'),
    path("serialNumberid/<int:id>", views.GenerateSerialSingle , name="Generate_Single_SerialNumber"),
    path("getPartNumber/<int:id>", views.GetPartNumber, name="PartNumber"),   
    path('customerProducts/', views.CustomerProducts, name="Customer_Products"),
    path('NewCustomerProducts/', views.NewCustomerProducts, name="New_Customer_Products")
]