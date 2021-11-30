import os
import datetime
from django.core.files.base import File
from django.core.paginator import Paginator
from django.forms.widgets import SelectMultiple
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from produtos.models import CategoriaProduto, ClasseProduto, NumeroSerie, Produto, Item, Arquivo, ProdutoCliente, Segmento, TipoProduto
from produtos.forms import CategoryForm, ClassProductForm, CustomerProductsForm, ItemForm, ProdutoForm, FileForm, SegmentForm, SerialNumberForm, TipForm, WorkOrderForm, produtoSelect

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
        context = {
            'products' : products
        }
    return render(request, 'produtos/Products.html', context)

def AddAllProduct(request):
    return render(request, 'produtos/AddAll.html')

def UpdateAllProduct(request):
    return render(request, 'produtos/UpdateAll.html')

def NewProduct(request):
    createProduct = ProdutoForm()
    if request.method == 'POST':
        createProduct = ProdutoForm(request.POST or None)
        if createProduct.is_valid():
            product = createProduct.save(commit = False)
            product.descontinuado = False
            product.save()
            return redirect('../../')
        
    else:
        createProduct = ProdutoForm()
    
    context = {
        'createProduct' : createProduct
    }
            
    return render(request, 'produtos/NewProduct.html', context)

def NewItem(request):
    createItem = ItemForm()
    if request.method == 'POST':
        createItem = ItemForm(request.POST, request.FILES)
        if createItem.is_valid():
            item = createItem.save(commit=False)
            item.tipo = 'Zip'
            item.save()
            return redirect('/products/')
    else:
        createItem = ItemForm()
    
    context = {
        'createItem' : createItem
    }
    
    return render(request, 'produtos/NewItem.html', context)

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

def NewSegment(request):
    createSegment = SegmentForm()
    if request.method == 'POST':
        createSegment = SegmentForm(request.POST or None)
        if createSegment.is_valid():
            createSegment.save()
            return redirect('/products')
        
    else:
        createSegment = SegmentForm()
    
    context = {
        'createSegment' : createSegment
    }
    
    return render(request, 'produtos/NewSegment.html', context)

def NewProductTip(request):
    createTip = TipForm()
    if request.method == 'POST':
        createTip = TipForm(request.POST or None)
        if createTip.is_valid():
            createTip.save()
            return redirect('/products')
        
    else:
        createTip = TipForm()
    
    context = {
        'createTip' : createTip
    }
    
    return render(request, 'produtos/NewProductTip.html', context)

def NewCategory(request):
    createCategory = CategoryForm()
    if request.method == 'POST':
        createCategory = CategoryForm(request.POST or None)
        if createCategory.is_valid():
            createCategory.save()
            return redirect('/products')
        
    else:
        createCategory = CategoryForm()
    
    context = {
        'createCategory' : createCategory
    }
    
    return render(request, 'produtos/NewCategory.html', context)

def NewClass(request):
    createClassProduct = ClassProductForm()
    if request.method == 'POST':
        createClassProduct = ClassProductForm(request.POST or None)
        if createClassProduct.is_valid():
            createClassProduct.save()
            return redirect('/products')
        
    else:
        createClassProduct = ClassProductForm()
        
    context = {
        'createClassProduct' : createClassProduct
    }
    
    return render(request, 'produtos/NewClass.html', context)

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

def UpdateProduct(request, id):
    product = get_object_or_404(Produto, id = id)
    updateProduct = ProdutoForm(instance = product)
    if request.method == 'POST':
        updateProduct = ProdutoForm(request.POST or None, instance = product)
        if updateProduct.is_valid():
            updateProduct.save()
            return redirect('../')
        else:
            context = {
                'updateProduct' : updateProduct,
                'product' : product
            }
            return render(request, 'produtos/UpdateProduct.html', context)

    else:
        context = {
            'updateProduct' : updateProduct,
            'product' : product
        }
        return render(request, 'produtos/UpdateProduct.html', context)

def UpdateSegment(request, id):
    segment = get_object_or_404(Segmento, id = id)
    updateSegment = SegmentForm(instance = segment)
    if request.method == 'POST':
        updateSegment = SegmentForm(request.POST or None, instance = segment)
        if updateSegment.is_valid():
            updateSegment.save()
            return redirect('../')
        else:
            context = {
                'updateSegment' : updateSegment,
                'segment' : segment
            }
            return render(request, 'produtos/UpdateSegment.html', context)
    
    else:
        context = {
            'updateSegment' : updateSegment,
            'segment' : segment
        }
        return render(request, 'produtos/UpdateSegment.html', context)

def UpdateProductTip(request, id):
    productTip = get_object_or_404(TipoProduto, id = id)
    updateTip = TipForm(instance = productTip)
    if request.method == 'POST':
        updateTip = TipForm(request.POST or None, instance = productTip)
        if updateTip.is_valid():
            updateTip.save()
            return redirect('../')
        else:
            context = {
                'updateTip' : updateTip,
                'productTip' : productTip
            }
            return render(request, 'produtos/UpdateProductTip.html', context)

    else:
        context = {
            'updateTip' : updateTip,
            'productTip' : productTip
        }
        return render(request, 'produtos/UpdateProductTip.html', context)

def UpdateCategory(request, id):
    category = get_object_or_404(CategoriaProduto, id = id)
    updateCategory = CategoryForm(instance = category)
    if request.method == 'POST':
        updateCategory = CategoryForm(request.POST or None, instance = category)
        if updateCategory.is_valid():
            updateCategory.save()
            return redirect('../')
        else:
            context = {
                'updateCategory' : updateCategory,
                'category' : category
            }
            return render(request, 'produtos/UpdateCategory.html', context)

    else:
        context = {
            'updateCategory' : updateCategory,
            'category' : category
        }
        return render(request, 'produtos/UpdateCategory.html', context)

def UpdateClass(request, id):
    classProduct = get_object_or_404(ClasseProduto, id = id)
    updateClassProduct = ClassProductForm(instance = classProduct)
    if request.method == 'POST':
        updateClassProduct = ClassProductForm(request.POST or None, instance = classProduct)
        if updateClassProduct.is_valid():
            updateClassProduct.save()
            return redirect('../')
        else:
            context = {
                'updateClassProduct' : updateClassProduct,
                'classProduct' : classProduct
            }
            return render(request, 'produtos/UpdateClass.html', context)

    else:
        context = {
            'updateClassProduct' : updateClassProduct,
            'classProduct' : classProduct
        }
        return render(request, 'produtos/UpdateClass.html', context)


# def DownloadItem(request, path):
#     filePath = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(filePath):
#         with open(filePath, 'rb') as fh:
#             response = HttpResponse(mimetype='application/force-download')
    #filePath = '/media/produtos'

def DeleteProduct(request, id):
    product = get_object_or_404(Produto, id = id)
    if request.method == 'POST':
        product.delete()
        return redirect('../')
    
    context = {'product' : product}
    return render(request, 'produtos/DeleteProduct.html', context)

def DeleteItem(request, id):
    item = get_object_or_404(Item, id = id)
    if request.method == 'POST':
        item.delete()
        return redirect('../')
    context = {'item' : item}
    return render(request, 'produtos/DeleteItem.html', context)

def DeleteFile(request, id):
    file = get_object_or_404(Arquivo, id = id)
    if request.method == 'POST':
        file.delete()
    context = {'file' : file}
    return render(request, 'produtos/DeleteFile.html', context)

def DeleteSegment(request, id):
    segment = get_object_or_404(Segmento, id = id)
    if request.method == 'POST':
        segment.delete()
    context = {'segment' : segment}
    return render(request, 'produtos/DeleteSegment.html', context)

def DeleteProductTip(request, id):
    productTip = get_object_or_404(TipoProduto, id = id)
    if request.method == 'POST':
        productTip.delete()
    context = {'productTip' : productTip}
    return render(request, 'produtos/DeleteProductTip.html', context)

def DeleteCategory(request, id):
    category = get_object_or_404(CategoriaProduto, id = id)
    if request.method == 'POST':
        category.delete()
    context = {'category' : category}
    return render(request, 'produtos/DeleteCategory.html', context)

def DeleteClassProduct(request, id):
    classProduct = get_object_or_404(ClasseProduto, id = id)
    if request.method == 'POST':
        classProduct.delete()
    context = {'classProduct' : classProduct}
    return render(request, 'produtos/DeleteClassProduct.html', context)

def SerialNumber(request):
    productsList = Produto.objects.all()
    serialNumbers = NumeroSerie.objects.all()
    context = {'serialNumbers' : serialNumbers, 'productsList' : productsList}
    return render(request, 'produtos/SerialNumber.html', context)

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
                fix = product.tipoProduto.sigla
                sufix = product.id
                var = 100
                os.serialNumber = str(prefix) + fix + str(sufix) + str(var)
                
            elif int(lastProduct.serialNumber[0:4]) != int(datetime.date.today().year):
                prefix = datetime.date.today().year
                fix = product.tipoProduto.sigla
                sufix = product.id
                var = 100
                os.serialNumber = str(prefix) + fix + str(sufix) + str(var)
           
            else:
                prefix = datetime.date.today().year
                fix = product.tipoProduto.sigla
                sufix = product.id
                var = int(lastProduct.serialNumber[7:10])
                var += 1
                os.serialNumber = str(prefix) + fix + str(sufix) + str(var)
            
            os.save()
            
    else:
        serialNumberForm = SerialNumberForm()
    
    return render(request, 'produtos/SerialNumberid.html', {'serialNumberForm': serialNumberForm})

def CustomerProducts(request):
    customerProduct = ProdutoCliente.objects.all()
    context = {'customerProduct' : customerProduct}
    return render(request, 'produtos/CustomerProducts.html', context)

def NewCustomerProducts(request):
    createCustomerProducts = CustomerProductsForm()
    if request.method == 'POST':
        createCustomerProducts = CustomerProductsForm(request.POST or None)
        if createCustomerProducts.is_valid():
            createCustomerProducts.save()
            return redirect('/products')
        
    else:
        createCustomerProducts = CustomerProductsForm()
        
    context = {
        'createCustomerProducts' : createCustomerProducts
    }
    return render(request, 'produtos/NewCustomerProducts.html', context)