from django.db import models
from django.db.models.fields import CharField, DateTimeField, EmailField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField
from django.db.models.fields.reverse_related import ManyToManyRel, ManyToOneRel
from django.urls.base import reverse
from departments.models import Departamento

class Colaborador(models.Model):
    nome = CharField(max_length=120)
    cargo = CharField(max_length=30)
    email = EmailField(null=True)
    user = OneToOneField(User, on_delete=models.CASCADE)
    departamento = ForeignKey(Departamento, on_delete=models.CASCADE)

    dateCriacao = DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('Home_Colaborator')

    def __str__(self):
        return self.nome