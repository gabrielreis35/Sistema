import os
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, PROTECT, SET, SET_NULL
from django.db.models.fields import  CharField, DateTimeField, IntegerField, FloatField
from django.db import models
from django.db.models.fields.related import ForeignKey
from colaborator.models import Colaborador
from workOrder.models import OrdemServico

class Segmento(models.Model):
    nome = CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.nome
    
class TipoProduto(models.Model):
    nome = CharField(max_length=40, unique=True)
    
    def __str__(self):
        return self.nome

class CategoriaProduto(models.Model):
    nome = CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nome
    
class ClasseProduto(models.Model):
    nome = CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    # tipoProduto = (
    #     ('AC', 'Acessório'),
    #     ('CC', 'Carregadeira'),
    #     ('CD', 'Chapa de desgaste'),
    #     ('CB', 'Chock bar'),
    #     ('DF', 'Dispositivos e ferramentas'),
    #     ('ER', 'Engate rápido'),
    #     ('CE', 'Escavadeira'),
    #     ('FP', 'Ferramenta de penetração de solo'),
    #     ('GA', 'Garfo'),
    #     ('CG', 'Graniteira'),
    #     ('LA', 'Lâmina'),
    #     ('LN', 'Lança'),
    #     ('RI', 'Ripper'),
    #     ('SG', 'Segmento'),
    #     ('VA', 'Vala'),
    #     ('SE', 'Serviço'),
    # )        
    # classeProduto = (
    #     ('6 SW', '6 SW'),
    #     ('6 LH', '6 LH'),
    #     ('7 SW', '7 SW'),
    #     ('7 LH', '7 LH'),
    #     ('7S SW', '7S SW'),
    #     ('7S LH', '7S LH'),
    #     ('8 SW', '8 SW'),
    #     ('8 LH', '8 LH'),
    #     ('9 SW', '9 SW'),
    #     ('9 LH', '9 LH'),
    #     ('9S SW', '9S SW'),
    #     ('9S LH', '9S LH'),
    # )
    # dureza = (
    #     ('GD', 'Geral'),
    #     ('HD', 'Pesada'),
    #     ('SD', 'Severa'),
    #     ('XD', 'Extrema'),
    # )

    nome = CharField(max_length=30)
    equipamento = CharField(max_length=10)
    capacidade = FloatField()
    largura = IntegerField()
    lamina = IntegerField()
    peso = IntegerField()
    
    dateCriacao = DateTimeField(auto_now_add=True)
    dateUpdate = DateTimeField(auto_now=True)

    segmento = ForeignKey(Segmento, null=True, on_delete=SET_NULL)
    tipoProduto = ForeignKey(TipoProduto, null=True, on_delete=SET_NULL)
    categoria = ForeignKey(CategoriaProduto, null=True, on_delete=SET_NULL)
    classeAplicacao = ForeignKey(ClasseProduto, null=True, on_delete=SET_NULL)
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

    revisao = IntegerField()
    nome = CharField(max_length=30)
    tipo = CharField(max_length=8)
    partNumber = CharField(max_length=16, null=True)
    tipoFabricacao = CharField(max_length=25, choices=tipoFabricacaoChoice)

    file = models.FileField(upload_to=filePath)

    dateCriacao = DateTimeField(auto_now_add=True)

    produto = ForeignKey(Produto, on_delete=CASCADE)

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

    revisao = IntegerField()
    nome = CharField(max_length=30)
    tipo = CharField(max_length=4, choices=tipoArquivo)
    partNumber = CharField(max_length=16, null=True)
    tipoFabricacao = CharField(max_length=25, choices=tipoFabricacaoChoice)
    file = models.FileField(upload_to=filePath)

    dateCriacao = DateTimeField(auto_now_add=True)

    produto = ForeignKey(Produto, null=True, blank=True, on_delete=CASCADE)

    def __str__(self):
        return self.nome
    
class NumeroSerie(models.Model):
    serialNumber = CharField(max_length=15, unique=True)
    
    os = ForeignKey(OrdemServico, unique=True, on_delete=CASCADE)
    produto = ForeignKey(Produto, unique=True, on_delete=CASCADE)
    
    def __str__(self):
        return self.id
    