from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Cliente

class ClientForm(ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'cnpj'
        ]
        
        labels = {
            'nome': ('Nome'),
            'cnpj': ('Cnpj')
        }