from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def Produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'Produtos.html', {'produtos' : produtos})

def viewProduto(request, id):
    produto = get_object_or_404(Produto, pk = id)
    return render(request, 'produto.html', {'produto' : produto})

def addProduto(request):
    formProduto = ProdutoForm(request.POST or None)
    if request.method == "POST":
        if formProduto.is_valid():
            formProduto.save()
            return redirect('/produtos')
        else:
            print(forms.ValidationError)

    return render(request, 'addProduto.html', {'formProduto' : formProduto})