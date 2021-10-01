from django.core.paginator import Paginator
import colaborator
from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from colaborator.models import Colaborador
from departments.models import Departamento
#from .models import Colaborador

def ViewColaborator(request):
    #colaborator = get_object_or_404(Colaborador)
    return render(request, 'colaborator/user.html')

def RegisterColaborator(request):
    search = request.GET.get('search')

    if search:
        colaborator = Colaborador.objects.filter(nome__icontains = search, departamento__icontains = search)
    else:
        colaboratorsList = Colaborador.objects.all()
        paginator = Paginator(colaboratorsList)
        page = request.GET.get('page')
        colaborator = paginator.get_page(page)
    return render(request, 'Register.html', {'colaborator' : colaborator})

