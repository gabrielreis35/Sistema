from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields
from django.forms.fields import EmailField

class SignupForm(UserCreationForm):
    nome = forms.CharField(max_length=30, required=True)
    sobrenome = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=150, required=True)
    cargo = forms.CharField(max_length=50, required=True)
    departamento = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
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