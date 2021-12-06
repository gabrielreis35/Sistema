from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from .models import Colaborador
from django.db import models
from django.forms import fields
from django.forms.fields import EmailField

class SignupForm(forms.Form):
    class Meta:
        model = Colaborador
        fields = [
            'username',
            'nome',
            'sobrenome',
            'email',
            'cargo',
            'departamento',
            'password1',
            'password2',
        ]

        labels = {
            'username': ('Nome de usuário'),
            'nome': ('Nome'),
            'sobrenome': ('Sobrenome'),
            'email': ('Email'),
            'cargo': ('Cargo'),
            'departamento': ('Departamento'),
            'password1': ('Senha'),
            'password2': ('Confirme sua senha') 
        }