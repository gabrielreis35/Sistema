from django import forms
from django.forms import ModelForm
from .models import Item, Produto, Arquivo

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
            'dureza'
        ]
        

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = [
            'nome',
            'tipo',
            'revisao',
            'partNumber',
            'tipoFabricacao'
        ]

class FileForm(ModelForm):
    class Meta:
        model = Arquivo
        fields = [
            'nome',
            'tipo',
        ]