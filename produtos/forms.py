from os import name
from typing import Optional
from django import forms
from django.forms import ModelForm, widgets
from .models import Item, Produto, Arquivo

class produtoSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex = None, attrs = None):
        option: super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['name'] = value.instance.nome
        return super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = [
            'segmento',
            'numeroSerie',
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

        labels = {
            'segmento': ('Segmento'),
            'numeroSerie': ('Número de Série'),
            'nome': ('Nome'),
            'equipamento': ('Equipamento'),
            'capacidade': ('Capacidade'),
            'largura': ('Largura'),
            'lamina': ('Lâmina'),
            'peso': ('Peso'),
            'codigo': ('Código'),
            'classe': ('Classe'),
            'dureza': ('Dureza'),

        }


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = [
            'produto',
            'nome',
            'revisao',
            'partNumber',
            'tipoFabricacao',
            'file'
        ]

        labels = {
            'produto': 'Produto relacionado',
            'nome': 'Nome',
            'tipo': 'Tipo',
            'revisao': 'Revisão',
            'partNumber': 'PartNumber',
            'tipoFabricacao': 'Tipo de Fabricação',
            'file': 'Arquivo'
        }        
        

class FileForm(ModelForm):
    class Meta:
        model = Arquivo
        fields = [
            'produto',
            'nome',
            'tipo',
            'revisao',
            'partNumber',
            'tipoFabricacao',
            'file'
        ]

        labels = {
            'produto': 'Produto relacionado',
            'nome': 'Nome',
            'tipo': 'Tipo',
            'revisao': 'Revisão',
            'partNumber': 'PartNumber',
            'tipoFabricacao': 'Tipo de Fabricação',
            'file': 'Arquivo'
        }