from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def Products(request):
    products = Produto.objects.all().order_by('-dateCriacao')
    return render(request, 'Products.html', {'products' : products})

def NewProduct(request):
    data = {}
    producForm = ProdutoForm(request.POST or None)
    if producForm.is_valid():
        producForm.save()
        return redirect('/products')

    data ['productForm'] = producForm
    return render(request, 'NewProduct.html', data)
    
def ViewProduct(request, id):
    product = get_object_or_404(Produto, pk = id)
    return render(request, 'Product.html', {'product' : product})

def UpdateProduct(request, id):
    data = {}
    product = Produto.objects.get(id = id)
    formProduct = ProdutoForm(request.POST or None, instance = product)
    if formProduct.is_valid():
        formProduct.save()
        return redirect('/products')
    data ['product'] = product
    return render(request, 'NewProduct.html', data)

def DeleteProduct(request, id):
    product = Produto.objects.get(id = id)
    product.delete()
    return redirect('/products')