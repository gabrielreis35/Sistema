import os
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, PROTECT, SET, SET_NULL
from django.db.models.fields import  BooleanField, CharField, DateField, DateTimeField, IntegerField, FloatField
from django.db import models
from django.db.models.fields.files import FileField
from django.db.models.fields.related import ForeignKey, OneToOneField
from clients.models import Cliente
from colaborator.models import Colaborador
from workOrder.models import OrdemServico

class Segmento(models.Model):
    nome = CharField(max_length=25, unique=True)
    sigla = CharField(max_length=20, unique=True)
    dateCriacao = DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome
    
class TipoProduto(models.Model):
    nome = CharField(max_length=40, unique=True)
    sigla = CharField(max_length=3, unique=True)
    dateCriacao = DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome

class CategoriaProduto(models.Model):
    nome = CharField(max_length=25, unique=True)
    sigla = CharField(max_length=5, unique=True)
    dateCriacao = DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome
    
class ClasseProduto(models.Model):
    nome = CharField(max_length=25, unique=True)
    sigla = CharField(max_length=3, unique=True)
    dateCriacao = DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = CharField(max_length=30)
    equipamento = CharField(max_length=10)
    capacidade = FloatField()
    largura = IntegerField()
    comprimento = IntegerField()
    volume = IntegerField()
    espessura = IntegerField()
    peso = IntegerField()
    descontinuado = BooleanField()
    dateCriacao = DateTimeField(auto_now_add=True)
    dateUpdate = DateTimeField(auto_now=True)
    segmento = ForeignKey(Segmento, null=True, on_delete=SET_NULL)
    tipoProduto = ForeignKey(TipoProduto, null=True, on_delete=SET_NULL)
    categoria = ForeignKey(CategoriaProduto, null=True, blank=True, on_delete=SET_NULL)
    classeAplicacao = ForeignKey(ClasseProduto, null=True, on_delete=SET_NULL)
    responsavel = ForeignKey(Colaborador, null=True, on_delete=SET_NULL)
    def __str__(self):
        return self.nome

class Item(models.Model):
    def filePath(produto, file):
        return os.path.join('produtos', produto.nome, file)
    revisao = IntegerField()
    nome = CharField(max_length=40)
    tipo = CharField(max_length=8)
    file = models.FileField(upload_to=filePath)
    dateCriacao = DateTimeField(auto_now_add=True)
    produto = ForeignKey(Produto, on_delete=CASCADE)
    def __str__(self):
        return self.nome
    
class PartNumber(models.Model):
    partNumber = CharField(max_length=30)
    terceiro = CharField(max_length=30, blank=True)
    dateCriacao = DateTimeField(auto_now_add=True)
    produto = ForeignKey(Produto, on_delete=CASCADE)
    def __self__(self):
        return self.id

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
    tipoArquivoSLD = (
        ('M', 'Montagem'),
        ('P', 'Peça')
    )
    revisao = IntegerField()
    nome = CharField(max_length=30)
    tipo = CharField(max_length=4, choices=tipoArquivo)
    tipoArquivo = CharField(max_length=8, choices=tipoArquivoSLD)
    tipoFabricacao = CharField(max_length=25, choices=tipoFabricacaoChoice)
    file = models.FileField(upload_to=filePath)
    dateCriacao = DateTimeField(auto_now_add=True)
    partNumber = OneToOneField(PartNumber, null=True, on_delete=models.CASCADE)
    produto = ForeignKey(Produto, null=True, blank=True, on_delete=CASCADE)
    def __str__(self):
        return self.nome
    
class NumeroSerie(models.Model):
    serialNumber = CharField(max_length=15, unique=True)
    os = ForeignKey(OrdemServico, on_delete=CASCADE)
    produto = ForeignKey(Produto, on_delete=CASCADE)
    dateCriacao = DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id

class ProdutoCliente(models.Model):
    def filePath(produto, file):
        return os.path.join('produtos', produto, file) 
    numeroSerie = CharField(max_length=30, null=True)
    produto = CharField(max_length=30)
    file = FileField(upload_to=filePath, null=True, blank=True)
    cliente = ForeignKey(Cliente, on_delete=CASCADE)
    dateCriacao = DateTimeField(auto_now_add=True)
    def __self__(self):
        return self.id