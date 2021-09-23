import colaborator
from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
#from .models import Colaborador

def ViewColaborator(request):
    #colaborator = get_object_or_404(Colaborador)
    return render(request, 'colaborator/user.html')