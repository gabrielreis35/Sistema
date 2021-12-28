from django.db import models
from produtos.models import CategoriaProduto, ClasseProduto, Produto, Segmento, TipoProduto

class ConfiguracoesProduto(models.Model):
    produto = models.ForeignKey(Produto, verbose_name="produto", on_delete=models.CASCADE)
    segmento = models.ForeignKey(Segmento, verbose_name="segmento", on_delete=models.CASCADE)
    tipoProduto = models.ForeignKey(TipoProduto, verbose_name="tipo de produto", on_delete=models.CASCADE)
    categoriaProduto = models.ForeignKey(CategoriaProduto, verbose_name="Categoria de produto", on_delete=models.CASCADE)
    classeProduto = models.ForeignKey(ClasseProduto, verbose_name="Classe de produto", on_delete=models.CASCADE)