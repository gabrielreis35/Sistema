from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField
from django.db.models.fields.related import ForeignKey

class OrdemServico(models.Model):
    OS = CharField(max_length=30, unique=True)
    
    dateCriacao = DateField(auto_now_add=True)
    
    def __str__(self):
        return self.OS