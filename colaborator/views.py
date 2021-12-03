from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from colaborator.models import Colaborador

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

@login_required
def ColaboratorRegister(request):
    colaborators = Colaborador.objects.all()
    context = {
        'colaborators' : colaborators
    }
    
    return render(request, 'colaborator/Signup.html', context)