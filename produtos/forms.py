from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('title', 'equipamento', 'volume', 'largura', 'lamina', 'peso', 'produto')