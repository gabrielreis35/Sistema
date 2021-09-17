from django.db import models
from django.db.models.fields import CharField

class Departamento(models.Model):
    nome = CharField(max_length=30)

    def __str__(self):
        return self.nome