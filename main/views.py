from django.shortcuts import get_object_or_404, render
from .models import Informacoes
# from django.contrib import messages

def Home(request):
    # colaborator = Informacoes()
    return render(request, 'main/Home.html')

def Login(request):
    return render(request, 'main/Login.html')