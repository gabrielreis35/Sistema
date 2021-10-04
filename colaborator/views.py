from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from colaborator.models import Colaborador
from departments.models import Departamento
from .forms import SignupForm
#from .models import Colaborador

def ViewColaborator(request):
    search = request.GET.get('search')
    if search:
        colaborator = Colaborador.objects.filter(nome__icontains = search, departamento__icontains = search)
    else:
        colaboratorsList = Colaborador.objects.all()
        paginator = Paginator(colaboratorsList, 20)
        page = request.GET.get('page')
        colaborator = paginator.get_page(page)
    return render(request, 'colaborator/User.html', {'colaborator' : colaborator})

def RegisterColaborator(request):
    if request.method == 'POST':
        signupForm = SignupForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            username = signupForm.cleaned_data.get('username')
            raw_passowrd = signupForm.cleaned_data.get('password1')
            messages.success(request, f'Conta criada com sucesso para {username}!')
            user = authenticate(username=username, password=raw_passowrd)
            login(request, user)
            return redirect('Home')
    else:
        signupForm = SignupForm()
    return render(request, 'colaborator/Signup.html', {'signupForm' : signupForm})