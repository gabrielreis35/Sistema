import os
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, PROTECT, SET_NULL
from django.db.models.fields import  CharField, DateTimeField, IntegerField, FloatField
from django.db import models
from django.db.models.fields.related import ForeignKey
from colaborator.models import Colaborador

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

    segmento = CharField(max_length=30, choices=segmento, null=True)
    numeroSerie = CharField(max_length=30, null=True)
    nome = CharField(max_length=30, null=True)
    equipamento = CharField(max_length=10, null=True)
    capacidade = FloatField(null=True)
    largura = IntegerField(null=True)
    lamina = IntegerField(null=True)
    peso = IntegerField(null=True)
    codigo = CharField(max_length=2, choices=tipoProduto, null=True)
    categoria = CharField(max_length=5, choices=classeProduto, null=True)
    classeAplicacao = CharField(max_length=2, choices=dureza, null=True)

    dateCriacao = DateTimeField(auto_now_add=True)
    dateUpdate = DateTimeField(auto_now=True)

    responsavel = ForeignKey(Colaborador, null=True, on_delete=SET_NULL)
    
    def __str__(self):
        return self.nome

class Item(models.Model):

    def filePath(produto, file):
        return os.path.join('produtos', produto.nome, file)
    
    tipoFabricacaoChoice = (
        ('Montagem Geral', 'Montagem Geral'),
        ('Montagem', 'Montagem'),
        ('Usinagem', 'Usinagem'),
        ('Soldado', 'Conjunto Soldado'),
        ('CNC', 'Corte CNC'),
        ('CNC / Dobra', 'Corte CNC com Dobra'),
        ('CNC / Usinagem', 'Corte CNC com Usinagem'),
        ('CNC / Dobra / Usinagem', 'Corte CNC com Dobra e Usinagem'),
        ('Manual', 'Corte Manual'),
        ('Manual / Dobra', 'Corte Manual com Dobra'),
        ('Manual / Usinagem', 'Corte Manual com Usinagem'),
        ('Manual / Dobra / Usinagem', 'Corte Manual com Dobra e Usinagem')
    )

    revisao = IntegerField(null=True)
    nome = CharField(max_length=30)
    tipo = CharField(max_length=8)
    partNumber = CharField(max_length=16, null=True)
    tipoFabricacao = CharField(max_length=25, choices=tipoFabricacaoChoice)

    file = models.FileField(upload_to=filePath)

    dateCriacao = DateTimeField(auto_now_add=True)

    produto = ForeignKey(Produto, null=True, on_delete=CASCADE)

    def __str__(self):
        return self.nome

class Arquivo(models.Model):
    def filePath(produto, file):
        return os.path.join('produtos', produto.nome, file)

    tipoArquivo = (
        ('DWG', 'DWG' ),
        ('DXF', 'DXF'),
        ('eDRA', 'eDrawing'),
        ('PDF', 'PDF')
    )
    
    tipoFabricacaoChoice = (
        ('Montagem Geral', 'Montagem Geral'),
        ('Montagem', 'Montagem'),
        ('Usinagem', 'Usinagem'),
        ('Soldado', 'Conjunto Soldado'),
        ('CNC', 'Corte CNC'),
        ('CNC / Dobra', 'Corte CNC com Dobra'),
        ('CNC / Usinagem', 'Corte CNC com Usinagem'),
        ('CNC / Dobra / Usinagem', 'Corte CNC com Dobra e Usinagem'),
        ('Manual', 'Corte Manual'),
        ('Manual / Dobra', 'Corte Manual com Dobra'),
        ('Manual / Usinagem', 'Corte Manual com Usinagem'),
        ('Manual / Dobra / Usinagem', 'Corte Manual com Dobra e Usinagem')
    )

    revisao = IntegerField(null=True)
    nome = CharField(max_length=30)
    tipo = CharField(max_length=4, choices=tipoArquivo)
    partNumber = CharField(max_length=16, null=True)
    tipoFabricacao = CharField(max_length=25, choices=tipoFabricacaoChoice)
    file = models.FileField(upload_to=filePath)

    dateCriacao = DateTimeField(auto_now_add=True)

    produto = ForeignKey(Produto, null=True, blank=True, on_delete=CASCADE)

    def __str__(self):
        return self.nome