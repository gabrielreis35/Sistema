from django.db.models.fields import CharField, DateTimeField, IntegerField
from django.db import models
from django.shortcuts import redirect

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

    dureza = (
        ('GD', 'Geral'),
        ('HD', 'Pesada'),
        ('SD', 'Severa'),
        ('XD', 'Extrema'),
    )

    segmentoProduto = models.CharField(max_length = 30, choices = segmento, null = True)
    nomeProduto = models.CharField(max_length = 30, null = True)
    equipamento = models.CharField(max_length = 10, null = True)
    capacidadeProduto = models.FloatField(null = True)
    larguraProduto = models.IntegerField(null = True)
    laminaProduto = models.IntegerField(null = True)
    pesoProduto = models.IntegerField(null = True)
    codigoProduto = models.CharField(max_length = 2, choices = tipoProduto, null = True)
    classeProduto = models.CharField(max_length = 5 ,null = True)
    partNumber = models.CharField(max_length = 16, null = True)
    numDentes = models.IntegerField(null = True)
    durezaProduto = models.CharField(max_length = 2, choices = dureza, null = True)

    dateCriacao = DateTimeField(auto_now_add = True)
    dateUpdate = DateTimeField(auto_now = True)

    
    def __str__(self):
        return self.nomeProduto