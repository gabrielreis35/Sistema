from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from colaborator.models import Colaborador

@login_required
def ColaboratorView(request):
    search = request.GET.get('search')
    colaboratorsList = Colaborador.objects.all().order_by('-dateCriacao')
    
    if search:
        colaboratorsList = Colaborador.objects.filter(nome__icontains = search)
    
    paginator = Paginator(colaboratorsList, 10)
    page = request.GET.get('page')
    colaborators = paginator.get_page(page)
    
    context = {
        'colaborators' : colaborators
    }
    return render(request, 'colaborator/User.html', context) 

@login_required
def ColaboratorRegister(request):
    createColaborator = ColaboratorRegister()
    # if request.method == 'POST':
    #     createColaborator = c
    
    
    context = {
        'colaborators' : createColaborator
    }
    
    return render(request, 'colaborator/Signup.html', context)