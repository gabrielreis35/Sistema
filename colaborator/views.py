from typing import List
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.widgets import Textarea
from django.views.generic import CreateView
#from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from colaborator.models import Colaborador
from django.forms import Textarea

class ColaboratorView(ListView):
    model = Colaborador

    def get_queryset(self):
        return Colaborador.objects.all

class ColaboratorRegister(CreateView):
    model = Colaborador
    fields = ['nome', 'cargo', 'departamento']
    labels = {'nome': 'Nome', 'cargo': 'Cargo', 'departamento': 'Departamento'}
    widgets = {
        'nome': Textarea(attrs={'placeholder': 'Nome Completo'}),
    }   

    def form_valid(self, form):
        colaborators = form.save(commit=False)
        first = colaborators.nome.split(' ')[0]
        last = colaborators.nome.split(' ')[1]
        username = first + last
        colaborators.user = User.objects.create(username = username)
        colaborators.save()
        return super(ColaboratorRegister, self).form_valid(form)