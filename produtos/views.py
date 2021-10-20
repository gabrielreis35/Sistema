import os
from django import forms
from django.core.files.base import File
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from produtos.models import Produto, Item, Arquivo
from produtos.forms import ItemForm, ProdutoForm, FileForm


def Products(request):
    search = request.GET.get('search')
    
    if search:
        products = Produto.objects.filter(nome__icontains = search, codigo__icontains = search)
    else:
        productsList = Produto.objects.all().order_by('-dateCriacao')
        paginator = Paginator(productsList, 20)
        page = request.GET.get('page')
        products = paginator.get_page(page)
    return render(request, 'produtos/Products.html', {'products' : products})

def NewProduct(request):
    productForm = ProdutoForm()
    if request.method == 'POST':
        productForm = ProdutoForm(request.POST or None)
        if productForm.is_valid():
            productForm.save()
            return redirect('/products')
        
    else:
        productForm = ProdutoForm()
        
    return render(request, 'produtos/NewProduct.html', {'productForm' : productForm})

def ViewProduct(request, id):
    context = []
    items = Item.objects.all().filter(produto_id = id).order_by('-revisao')
    files = Arquivo.objects.all().filter(produto_id = id).order_by('-revisao')
    product = get_object_or_404(Produto, id = id)
    context = {
        'product': product,
        'items': items,
        'files': files,
    }
    return render(request, 'produtos/Product.html', context)

def UpdateProduct(request, id):
    product = get_object_or_404(Produto, id = id)
    productForm = ProdutoForm(instance = product)
    if request.method == 'POST':
        productForm = ProdutoForm(request.POST or None, instance = product)
        if productForm.is_valid():
            productForm.save()
            return redirect('../')
        else:
            return render(request, 'produtos/UpdateProduct.html', {'productForm' : productForm, 'product' : product})

    else:    
        return render(request, 'produtos/UpdateProduct.html', {'productForm' : productForm, 'product' : product})


def DeleteProduct(request, id):
    product = get_object_or_404(Produto, id = id)
    product.delete()
    messages.info(request, 'Produto excluído')
    return redirect('/products')


def NewItem(request):
    itemForm = ItemForm()
    if request.method == 'POST':
        itemForm = ItemForm(request.POST, request.FILES)
        if itemForm.is_valid():
            item = itemForm.save(commit=False)
            item.tipo = 'Zip'
            item.save()
            return redirect('/products/')
    else:
        itemForm = ItemForm()
    return render(request, 'produtos/NewItem.html', {'itemForm' : itemForm})

# def DownloadItem(request, id):
#     item = Item()
#     product = Produto()
#     filePath = '/media/produtos' + product.nome


def DeleteItem(request, id):
    item = get_object_or_404(Item, id = id)
    item.delete()
    messages.info(request, 'Item excluído')
    return redirect('/products')


def NewFile(request):
    fileForm = FileForm()
    if request.method == 'POST':
        fileForm = FileForm(request.POST, request.FILES)
        if fileForm.is_valid():
            fileForm.save()
            return redirect('/products/')
        
    else:
        fileForm = FileForm()
        
    return render(request, 'produtos/NewFile.html', {'fileForm' : fileForm})


def DeleteFile(request, id):
    file = get_object_or_404(Arquivo, id = id)
    file.delete()
    messages.info(request, 'Arquivo excluído')
    return redirect('/products')
