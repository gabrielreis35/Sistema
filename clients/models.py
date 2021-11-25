from django.db import models
from django.db.models.fields import CharField, DateTimeField, IntegerField

class Cliente(models.Model):
    nome = CharField(max_length=50)
    cnpj = IntegerField()
    
    dateCriacao = DateTimeField(auto_now_add=True)
    
    def __self__(self):
        return self.nome