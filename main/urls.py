from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.Home, name = 'Home'),
    path('main/', include('django.contrib.auth.urls')),
]
