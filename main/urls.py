from django.urls import path
from django.urls.conf import include
from . import views

app_name = "main"

urlpatterns = [
    path('', views.Home, name = 'Home_Main'),
]
