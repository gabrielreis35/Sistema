from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def Products(request):
    products = Produto.objects.all().order_by('-dateCriacao')
    return render(request, 'Products.html', {'products' : products})

def ViewProduct(request, id):
    product = get_object_or_404(Produto, pk = id)
    return render(request, 'Product.html', {'product' : product})

def NewProduct(request):
    producForm = ProdutoForm()
    if request.method == 'POST':
        producForm(request.POST or None)
        if producForm.is_valid():
            producForm.save()
            return redirect('/products')

    producForm = ProdutoForm()
    return render(request, 'NewProduct.html', {'productForm' : producForm})