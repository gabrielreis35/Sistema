from django.db import models
from django.urls import reverse
from django.db.models.fields import CharField

class Departamento(models.Model):
    nome = CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('Home_Departments')

    def __str__(self):
        return self.nome