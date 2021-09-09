from django.db.models.fields import DateTimeField, IntegerField
from django.db import models

class Produto(models.Model):
    tipoProduto = (
        ('AC', 'Acessório'),
        ('CC', 'Carregadeira'),
        ('CD', 'Chapa de desgaste'),
        ('CB', 'Chock bar'),
        ('DF', 'Dispositivos e ferramentas'),
        ('ER', 'Engate rápido'),
        ('CE', 'Escavadeira'),
        ('FP', 'Ferramenta de penetração de solo'),
        ('GA', 'Garfo'),
        ('CG', 'Graniteira'),
        ('LA', 'Lâmina'),
        ('LN', 'Lança'),
        ('RI', 'Ripper'),
        ('SG', 'Segmento'),
        ('VA', 'Vala'),
        ('SE', 'Serviço'),
    )
    title = models.CharField(max_length = 30)
    equipamento = models.CharField(max_length = 10)
    volume = models.IntegerField()
    largura = models.FloatField()
    lamina = models.IntegerField()
    peso = models.FloatField()
    produto = models.CharField(max_length = 2, choices = tipoProduto)
    codigoProduto = IntegerField()
    dateCriacao = DateTimeField(auto_now_add = True)
    dateUpdate = DateTimeField(auto_now = True)