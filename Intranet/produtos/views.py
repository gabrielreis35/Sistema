from django.shortcuts import render, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def Produtos(request):
    products = Produto.objects.all()
    return render(request, 'Produtos.html', {'produtos' : products})

def viewProduto(request, id):
    produto = get_object_or_404(Produto, pk = id)
    return render(request, 'produto.html', {'produto' : produto})

def addProduto(request):
    form = ProdutoForm()
    return render(request, 'addProduto.html', {'form' : form})