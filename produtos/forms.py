from os import name
from typing import Optional
from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import CategoriaProduto, ClasseProduto, Item, NumeroSerie, Produto, Arquivo, Segmento, TipoProduto
from workOrder.models import OrdemServico

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
            'nome',
            'equipamento',
            'capacidade',
            'largura',
            'lamina',
            'peso',
            'tipoProduto',
            'categoria',
            'classeAplicacao'
        ]

        labels = {
            'segmento': ('Segmento'),
            'nome': ('Nome'),
            'equipamento': ('Equipamento'),
            'capacidade': ('Capacidade'),
            'largura': ('Largura'),
            'lamina': ('Lâmina'),
            'peso': ('Peso'),
            'tipoProduto': ('Tipo de Produto'),
            'categoria': ('Categoria'),
            'classeAplicacao': ('Classe se Aplicação'),

        }

class SegmentForm(ModelForm):
    class Meta:
        model = Segmento
        fields = [
            'nome',
            'sigla'
        ]
        labels = {
            'nome': ('Nome:'),
            'sigla': ('Sigla:')
        }

class TipForm(ModelForm):
    class Meta:
        model = TipoProduto
        fields = [
            'nome',
            'sigla'
        ]
        labels = {
            'nome': ('Nome:'),
            'sigla': ('Sigla:')
        }
        
class CategoryForm(ModelForm):
    class Meta:
        model = CategoriaProduto
        fields = [
            'nome',
            'sigla'
        ]
        labels = {
            'nome': ('Nome:'),
            'sigla': ('Sigla:')
        }
        
class ClassProductForm(ModelForm):
    class Meta:
        model = ClasseProduto
        fields = [
            'nome',
            'sigla'
        ]
        labels = {
            'nome': ('Nome:'),
            'sigla': ('Sigla:')
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
            'produto': ('Produto relacionado'),
            'nome': ('Nome'),
            'tipo': ('Tipo'),
            'revisao': ('Revisão'),
            'partNumber': ('PartNumber'),
            'tipoFabricacao': ('Tipo de Fabricação'),
            'file': ('Arquivo')
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
            'produto': ('Produto relacionado'),
            'nome': ('Nome'),
            'tipo': ('Tipo'),
            'revisao': ('Revisão'),
            'partNumber': ('PartNumber'),
            'tipoFabricacao': ('Tipo de Fabricação'),
            'file': ('Arquivo')
        }

class SerialNumberForm(ModelForm):
    class Meta:
        model = NumeroSerie
        fields = [
            'os',
            'produto',
        ]
        
        labels = {
            'os': ('Ordem de Serviço relacionada:'),
            'produto': ('Produto relacionado:')
        }

class WorkOrderForm(ModelForm):
    class Meta:
        model = OrdemServico
        fields = [
            'OS'
        ]