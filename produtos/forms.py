from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = (
            'segmentoProduto',
            'nomeProduto',
            'equipamento',
            'capacidadeProduto',
            'larguraProduto',
            'laminaProduto',
            'pesoProduto',
            'codigoProduto',
            'classeProduto',
            'partNumber',
            'numDentes',
            'durezaProduto')