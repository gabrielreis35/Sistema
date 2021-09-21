from django import forms
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from produtos.models import Produto
from produtos.forms import ProdutoForm

def Products(request):
    productsList = Produto.objects.all().order_by('-dateCriacao')
    paginator = Paginator(productsList, 20)
    page = request.GET.get('page')
    produtcs = paginator.get_page(page)
    return render(request, 'Products.html', {'products' : produtcs})

def NewProduct(request):
    productForm = ProdutoForm()
    if request.method == 'POST':
        productForm = ProdutoForm(request.POST or None)
        if productForm.is_valid():
            productForm.save()
            return redirect('/products')
        
    else:
        productForm = ProdutoForm()
        
    return render(request, 'NewProduct.html', {'productForm' : productForm})
    
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
    return render(request, 'UpdateProduct.html', data)

def DeleteProduct(request, id):
    product = Produto.objects.get(id = id)
    product.delete()
    return redirect('/products')

def NewItem(request):
    return render(request, 'NewItem.html')

def NewFile(request):
    return render(request, 'NewFile.html')