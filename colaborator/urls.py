from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViewColaborator, name = 'Colaborator'),
    path('register/', views.RegisterColaborator, name = 'Register_Colaborator'),
]
