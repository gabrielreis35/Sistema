from django.forms import ModelForm
from .models import Item, Produto, Arquivo

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
            'numeroSerie': ('Número de Série:'),
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
            'nome',
            'tipo',
            'revisao',
            'partNumber',
            'tipoFabricacao'
        ]

        labels = {
            'nome': 'Nome',
            'tipo': 'Tipo',
            'revisao': 'Revisão',
            'partNumber': 'PartNumber',
            'tipoFabricacao': 'Tipo de Fabricação'
        }

class FileForm(ModelForm):
    class Meta:
        model = Arquivo
        fields = [
            'nome',
            'tipo',
            'revisao',
            'partNumber',
            'tipoFabricacao'
        ]

        labels = {
            'nome': 'Nome',
            'tipo': 'Tipo',
            'revisao': 'Revisão',
            'partNumber': 'PartNumber',
            'tipoFabricacao': 'Tipo de Fabricação'
        }