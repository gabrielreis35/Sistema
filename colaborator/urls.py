from django.contrib import admin
from django.urls import path
from .views import ColaboratorView, ColaboratorRegister
app_name = 'colaborators'

urlpatterns = [
    path('users/', ColaboratorView, name = 'Home_Colaborator'),
    path('signup/', ColaboratorRegister, name='Signup_Colaborator')
]
