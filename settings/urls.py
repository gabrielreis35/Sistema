from django.urls import path
from . import views

app_name = "settings"

urlpatterns = [
    path('', views.Settings, name = 'Settings_Main'),
    path('products', views.ProductSettings, name = 'Product_Settings'),
    path('workorder', views.WorkOrderSettings, name = 'WorkOder_Settings')
]
