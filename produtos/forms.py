from django import forms
from django.forms import ModelForm
from .models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = [
            'segmento',
            'nome',
            'equipamento',
            'capacidade',
            'largura',
            'lamina',
            'peso',
            'codigo',
            'classe',
            'numDentes',
            'dureza']
        
        widgets = {
            'segmento': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Nome do produto'}),
            'equipamento': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Qual equipamento'}),
            'capacidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'em m³'}),
            'largura': forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'em mm'}),
            'lamina': forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'em mm'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'em kg'}),
            'codigo': forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Código do produto'}),
            'classe': forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Classe'}),
            'numDentes': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de dentes da caçamba'}),
            'dureza': forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Qual código de dureza o produto se encontra'}),
        }