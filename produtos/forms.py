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