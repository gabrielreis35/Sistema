from django import forms
from django.core.files.base import File
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from produtos.models import Produto, Item
from produtos.forms import ItemForm, ProdutoForm, FileForm

def Products(request):
    productsList = Produto.objects.all().order_by('-dateCriacao')
    paginator = Paginator(productsList, 20)
    page = request.GET.get('page')
    produtcs = paginator.get_page(page)
    return render(request, 'produtos/Products.html', {'products' : produtcs})

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
    item = Item.objects.all()
    product = get_object_or_404(Produto, pk = id)
    return render(request, 'produtos/Product.html', {'product' : product}, {'item' : item})

def UpdateProduct(request, id):
    data = {}
    product = Produto.objects.get(id = id)
    formProduct = ProdutoForm(request.POST or None, instance = product)
    if formProduct.is_valid():
        formProduct.save()
        return redirect('/products')
    data ['product'] = product
    return render(request, 'produtos/UpdateProduct.html', data)

def DeleteProduct(request, id):
    product = Produto.objects.get(id = id)
    product.delete()
    return redirect('/products')

def NewItem(request):
    itemForm = ItemForm()
    if request.method == 'POST':
        itemForm = ItemForm(request.POST or None)
        if itemForm.is_valid():
            itemForm.save()
            return redirect('/product/<int:id>')
        
    else:
        itemForm = ItemForm()
        
    return render(request, 'produtos/NewItem.html', {'itemForm' : itemForm})


def NewFile(request):
    fileForm = FileForm()
    if request.method == 'POST':
        fileForm = FileForm(request.POST or None)
        if fileForm.is_valid():
            fileForm.save()
            return redirect('/product/<int:id>')
        
    else:
        fileForm = FileForm()
        
    return render(request, 'produtos/NewFile.html', {'fileForm' : fileForm})