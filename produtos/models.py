from django.db.models.fields import  DateTimeField
from django.db import models
from django.http import request

class Produto(models.Model):
    segmento = (
        ('A', 'Agrícola'),
        ('C', 'Construção'),
        ('F', 'Florestal'),
        ('I', 'Industrial'),
        ('U', 'Automotiva'),
        ('M', 'Mineração'),
    )

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

    classeProduto = (
        ('6 SW', '6 SW'),
        ('6 LH', '6 LH'),
        ('7 SW', '7 SW'),
        ('7 LH', '7 LH'),
        ('7S SW', '7S SW'),
        ('7S LH', '7S LH'),
        ('8 SW', '8 SW'),
        ('8 LH', '8 LH'),
        ('9 SW', '9 SW'),
        ('9 LH', '9 LH'),
        ('9S SW', '9S SW'),
        ('9S LH', '9S LH'),
    )

    dureza = (
        ('GD', 'Geral'),
        ('HD', 'Pesada'),
        ('SD', 'Severa'),
        ('XD', 'Extrema'),
    )

    segmentoProduto = models.CharField(max_length = 30, choices = segmento)
    nomeProduto = models.CharField(max_length = 30)
    equipamento = models.CharField(max_length = 10)
    capacidadeProduto = models.FloatField()
    larguraProduto = models.IntegerField()
    laminaProduto = models.IntegerField()
    pesoProduto = models.IntegerField()
    codigoProduto = models.CharField(max_length = 2, choices = tipoProduto)
    classeProduto = models.CharField(max_length = 5, choices = classeProduto)
    partNumber = models.CharField(max_length = 16)
    numDentes = models.IntegerField()
    durezaProduto = models.CharField(max_length = 2, choices = dureza)

    dateCriacao = DateTimeField(auto_now_add = True)
    dateUpdate = DateTimeField(auto_now = True)

    
    def __str__(self):
        return self.nomeProduto