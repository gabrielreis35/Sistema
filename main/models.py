from django.db import models
from django.db.models.deletion import CASCADE
from colaborator.models import Colaborador
from django.db.models.fields.related import ForeignKey

class Informacoes(models.Model):
    colaborador = ForeignKey(Colaborador, null=True, on_delete=CASCADE)