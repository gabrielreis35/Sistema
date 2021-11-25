from django.urls import path
from . import views
from . import models

app_name = 'clients'

urlpatterns = [
    path('', views.HomeClients, name="Home_Clients"),
    path('addClient', views.NewClient, name="New_Client")
]