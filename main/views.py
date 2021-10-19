from django.contrib.auth import login
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Informacoes
# from django.contrib import messages

@login_required
def Home(request):
    # colaborator = Informacoes()
    return render(request, 'main/Home.html')