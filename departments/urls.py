from django.urls import path
from . import views

urlpatterns = [
    path('', views.Departments, name = 'Departments'),
]
