from django import forms
from .models import Produto

class ProdutoForm(forms.Form):
    class Meta:
        model = Produto
        fields = (
            'nomeProduto',
            'equipamento',
            'volume',
            'largura',
            'lamina',
            'peso',
            'produto',
            'codigoProduto')