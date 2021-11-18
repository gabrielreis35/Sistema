import os
import datetime
from django.core.files.base import File
from django.core.paginator import Paginator
from django.forms.widgets import SelectMultiple
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from produtos.models import CategoriaProduto, ClasseProduto, NumeroSerie, Produto, Item, Arquivo, Segmento, TipoProduto
from produtos.forms import CategoryForm, ClassProductForm, ItemForm, ProdutoForm, FileForm, SegmentForm, SerialNumberForm, TipForm, WorkOrderForm, produtoSelect

def Products(request):
    search = request.GET.get('search')
    
    if search:
        products = Produto.objects.filter(nome__icontains = search)
    else:
        productsList = Produto.objects.all().order_by('-dateCriacao')
        order = request.GET.get('order')
        
        if order:
            if order == 'Produto':
                productsList = Produto.objects.all().order_by('nome')
            elif order == 'Equipamento':
                productsList = Produto.objects.all().order_by('equipamento')
            elif order == 'Codigo':
                productsList = Produto.objects.all().order_by('codigo')
            elif order == 'Segmento':
                productsList = Produto.objects.all().order_by('segmento')
        
        paginator = Paginator(productsList, 20)
        page = request.GET.get('page')
        products = paginator.get_page(page)
    return render(request, 'produtos/Products.html', {'products' : products})

def AddAllProduct(request):
    return render(request, 'produtos/AddAll.html')

def UpdateAllProduct(request):
    return render(request, 'produtos/UpdateAll.html')

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

def NewSegment(request):
    segmentForm = SegmentForm()
    if request.method == 'POST':
        segmentForm = SegmentForm(request.POST or None)
        if segmentForm.is_valid():
            segmentForm.save()
            return redirect('/products')
        
    else:
        segmentForm = SegmentForm()
    return render(request, 'produtos/NewSegment.html', {'segmentForm' : segmentForm})

def NewProductTip(request):
    tipForm = TipForm()
    if request.method == 'POST':
        tipForm = TipForm(request.POST or None)
        if tipForm.is_valid():
            tipForm.save()
            return redirect('/products')
        
    else:
        tipForm = TipForm()
    return render(request, 'produtos/NewProductTip.html', {'tipForm' : tipForm})

def NewCategory(request):
    categoryForm = CategoryForm()
    if request.method == 'POST':
        categoryForm = CategoryForm(request.POST or None)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('/products')
        
    else:
        categoryForm = CategoryForm()
    return render(request, 'produtos/NewCategory.html', {'categoryForm' : categoryForm})

def NewClass(request):
    classProductForm = ClassProductForm()
    if request.method == 'POST':
        classProductForm = ClassProductForm(request.POST or None)
        if classProductForm.is_valid():
            classProductForm.save()
            return redirect('/products')
        
    else:
        classProductForm = ClassProductForm()
    return render(request, 'produtos/NewClass.html', {'classProductForm' : classProductForm})

def ViewSegment(request):
    segments = Segmento.objects.all().order_by('-dateCriacao')

    return render(request, 'produtos/ViewSegment.html', {'segments' : segments})

def ViewProductTip(request):
    productTipes = TipoProduto.objects.all().order_by('-dateCriacao')

    return render(request, 'produtos/ViewProductTip.html', {'productTipes' : productTipes})

def ViewCategory(request):
    categories = CategoriaProduto.objects.all().order_by('-dateCriacao')

    return render(request, 'produtos/ViewCategory.html', {'categories' : categories})

def ViewClass(request):
    classes = ClasseProduto.objects.all().order_by('-dateCriacao')

    return render(request, 'produtos/ViewClass.html', {'classes' : classes})

def UpdateSegment(request, id):
    segment = get_object_or_404(Segmento, id = id)
    segmentForm = SegmentForm(instance = segment)
    if request.method == 'POST':
        segmentForm = SegmentForm(request.POST or None, instance = segment)
        if segmentForm.is_valid():
            segmentForm.save()
            return redirect('../')
        else:
            return render(request, 'produtos/UpdateSegment.html', {'segmentForm' : segmentForm, 'segment' : segment})

    else:    
        return render(request, 'produtos/UpdateSegment.html')

def UpdateProductTip(request, id):
    productTip = get_object_or_404(TipoProduto, id = id)
    productTipForm = TipForm(instance = productTip)
    if request.method == 'POST':
        productTipForm = TipForm(request.POST or None, instance = productTip)
        if productTipForm.is_valid():
            productTipForm.save()
            return redirect('../')
        else:
            return render(request, 'produtos/UpdateProductTip.html', {'productTipForm' : productTipForm, 'productTip' : productTip})

    else:    
        return render(request, 'produtos/UpdateProductTip.html')

def UpdateCategory(request, id):
    category = get_object_or_404(CategoriaProduto, id = id)
    categoryForm = CategoryForm(instance = category)
    if request.method == 'POST':
        categoryForm = CategoryForm(request.POST or None, instance = category)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('../')
        else:
            return render(request, 'produtos/UpdateCategory.html', {'categoryForm' : categoryForm, 'category' : category})

    else:    
        return render(request, 'produtos/UpdateCategory.html')

def UpdateClass(request, id):
    classProduct = get_object_or_404(ClasseProduto, id = id)
    classForm = ClassProductForm(instance = classProduct)
    if request.method == 'POST':
        classForm = ClassProductForm(request.POST or None, instance = classProduct)
        if classForm.is_valid():
            classForm.save()
            return redirect('../')
        else:
            return render(request, 'produtos/UpdateClass.html', {'classForm' : classForm, 'classProduct' : classProduct})

    else:    
        return render(request, 'produtos/UpdateClass.html')

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
    productsList = Produto()
    generate = request.GET.get('generate')
    if generate:
        productsList = Produto.objects.filter(nome__icontains = generate)
    productsList = Produto.objects.all()
    
    # paginator = Paginator(productsList, 10)
    # page = request.GET.get('page')
    # productsList = paginator.get_page(page)
    return render(request, 'produtos/NewSerialNumber.html', {'products': productsList})

def GenerateSerialSingle(request, id):
    serialNumberForm = SerialNumberForm()
    product = Produto.objects.get(id=id)
    
    if request.method == 'POST':
        serialNumberForm = SerialNumberForm(request.POST or None)
        
        if serialNumberForm.is_valid():
            os = serialNumberForm.save(commit=False)
            os.numeroSerie = id
            lastProduct = NumeroSerie.objects.last()
            
            if lastProduct == None:
                prefix = datetime.date.today().year
                fix = product.nome[3:6]
                sufix = product.id
                var = 100
                os.serialNumber = str(prefix) + fix + str(sufix) + str(var)
                
            elif int(lastProduct.serialNumber[0:4]) != int(datetime.date.today().year):
                prefix = datetime.date.today().year
                fix = product.nome[3:6]
                sufix = product.id
                var = 100
                os.serialNumber = str(prefix) + fix + str(sufix) + str(var)
           
            else:
                prefix = datetime.date.today().year
                fix = product.nome[3:6]
                sufix = product.id
                var = int(lastProduct.serialNumber[8:11])
                var += 1
                os.serialNumber = str(prefix) + fix + str(sufix) + str(var)
            
            os.save()
            
    else:
        serialNumberForm = SerialNumberForm()
    
    return render(request, 'produtos/SerialNumberid.html', {'serialNumberForm': serialNumberForm})