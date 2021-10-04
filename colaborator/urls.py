from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViewColaborator, name = 'Colaborator'),
    path('signup/', views.RegisterColaborator, name = 'Signup_Colaborator'),
]
