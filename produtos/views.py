import os
import datetime
# from django import forms
# from django.conf import settings
from django.core.files.base import File
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from produtos.models import NumeroSerie, Produto, Item, Arquivo
from produtos.forms import ItemForm, ProdutoForm, FileForm, SerialNumberForm, WorkOrderForm
# from django.http import HttpResponse, Http404

def Products(request):
    search = request.GET.get('search')
    
    if search:
        products = Produto.objects.filter(nome__icontains = search)
    else:
        productsList = Produto.objects.all().order_by('-dateCriacao')
        
        order = request.GET.get('order')
        if order == 'Produto':
            productsList = Produto.objects.all().order_by('-nome')
        elif order == 'Equipamento':
            productsList = Produto.objects.all().order_by('equipamento')
        elif order == 'Codigo':
            productsList = Produto.objects.all().order_by('-codigo')
        elif order == 'Segmento':
            productsList = Produto.objects.all().order_by('-segmento')
        elif order == 'numSerie':
            productsList = Produto.objects.all().order_by('-numeroSerie')
        
        
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

# def DownloadItem(request, path):
#     filePath = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(filePath):
#         with open(filePath, 'rb') as fh:
#             response = HttpResponse(mimetype='application/force-download')
    #filePath = '/media/produtos'


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

def SerialNumber(request):
    return render(request, 'produtos/SerialNumber.html')

def GenerateSerial(request):
    generate = request.GET.get('generate')
    if generate:
        productsList = Produto.objects.filter(nome__icontains = generate)
    productsList = Produto.objects.all()
    
    paginator = Paginator(productsList, 10)
    page = request.GET.get('page')
    productsList = paginator.get_page(page)
    return render(request, 'produtos/NewSerialNumber.html', {'products': productsList})

def GenerateSerialSingle(request, id):
    data = {}
    product = Produto()
    if request.method == 'POST':
        data['os'] = WorkOrderForm(request.POST or None)
        if data['os'].is_valid():
            os = data['os'].save(commit=False)
            Produto.numeroSerie = NumeroSerie.id
            os.numeroSerie = id
            filter = Produto.objects.filter(id__icontains = id)
            lastProduct = filter.last(Produto.numeroSerie.serialNumber)
            
            if lastProduct[0, 1, 2, 3] != datetime.today().year:
                prefix = datetime.today().year
                fix = Produto.nome[3, 4, 5, 6]
                sufix = Produto.id
                var = 101
                NumeroSerie.serialNumber = prefix + fix + sufix + var
            else:
                prefix = datetime.today().year
                fix = Produto.nome[3, 4, 5, 6]
                sufix = Produto.id
                var = (lastProduct) =+ 1
                NumeroSerie.serialNumber = prefix + fix + sufix + var
            
    else:
        data['os'] = WorkOrderForm()
    
    return render(request, 'produtos/SerialNumberid.html', data, {'product':product})