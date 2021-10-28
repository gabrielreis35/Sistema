from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from django.forms.widgets import Textarea
from django.views.generic import CreateView
from colaborator.models import Colaborador
from django.forms import Textarea

@login_required
def ColaboratorView(request):
    search = request.GET.get('search')
    
    if search:
        colaborators = Colaborador.objects.filter(nome__icontains = search)
    else:
        # colaboratorsList = Colaborador
        # paginator = Paginator(colaboratorsList, 20)
        # page = request.GET.get('page')
        # paginator.get_page(page)
        colaborators = Colaborador.objects.all().order_by('-dateCriacao')
    return render(request, 'colaborator/User.html', {'colaborators' : colaborators}) 

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