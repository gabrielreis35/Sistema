from django.contrib.auth import login
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from produtos.models import Produto, TipoProduto

from .models import Informacoes
# from django.contrib import messages

@login_required
def Home(request):
    countProduct = Produto.objects.count()
    tipProduct = Produto.objects.filter(tipoProduto__nome = 'Graniteira').count()
    context = {
        'countProduct' : countProduct,
        'tipProduct' : tipProduct
    }
    return render(request, 'main/Home.html', context)