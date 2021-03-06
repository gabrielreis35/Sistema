import os
import datetime
from django.conf import settings
from django.http import HttpResponse
from django.core.files.base import File
from django.core.paginator import Paginator
from django.forms.widgets import SelectMultiple
from django.http import response
from django.http.response import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from produtos.models import CategoriaProduto, ClasseProduto, NumeroSerie, Produto, Item, Arquivo, ProdutoCliente, Segmento, TipoProduto, PartNumber
from produtos.forms import CategoryForm, ClassProductForm, CustomerProductsForm, ItemForm, PartNumberForm, ProdutoForm, FileForm, SegmentForm, SerialNumberForm, TipForm, WorkOrderForm, produtoSelect
from clients.models import Cliente
def Products(request):
    """  View of main page of products """
    search = request.GET.get('search')
    
    if search:
        productsList = Produto.objects.filter(nome__icontains = search)
        paginator = Paginator(productsList, 10)
        page = request.GET.get('page')
        products = paginator.get_page(page)
    else:
        productsList = Produto.objects.all().order_by('-dateCriacao')
        order = request.GET.get('order')
        if order == 'Produto':
            productsList = Produto.objects.all().order_by('nome')
        elif order == 'Equipamento':
            productsList = Produto.objects.all().order_by('equipamento')
        elif order == 'Codigo':
            productsList = Produto.objects.all().order_by('codigo')
        elif order == 'Segmento':
            productsList = Produto.objects.all().order_by('segmento')
            
        paginator = Paginator(productsList, 10)
        page = request.GET.get('page')
        products = paginator.get_page(page)
    context = {'products' : products}
    return render(request, 'produtos/Products.html', context)

def NewProduct(request):
    """  View of new product  """
    createProduct = ProdutoForm()
    if request.method == 'POST':
        createProduct = ProdutoForm(request.POST or None)
        if createProduct.is_valid():
            product = createProduct.save(commit = False)
            product.descontinuado = False
            product.save()
            return redirect('products:Home_Products')
    else:
        createProduct = ProdutoForm()
    context = {'createProduct' : createProduct}
    return render(request, 'produtos/NewProduct.html', context)

def NewItem(request, id):
    """  View of new items for products  """
    product = get_object_or_404(Produto, id=id)
    createItem = ItemForm()
    if request.method == 'POST':
        createItem = ItemForm(request.POST, request.FILES)
        if createItem.is_valid():
            item = createItem.save(commit=False)
            item.produto = product
            item.save()
            return redirect('produtos/View_Product', product)
    else:
        createItem = ItemForm()
    context = {'createItem' : createItem, 'product' : product}
    return render(request, 'produtos/NewItem.html', context)

def NewFile(request, id):
    """  view of new file  for products  """
    product = get_object_or_404(Produto, id=id)
    fileForm = FileForm()
    if request.method == 'POST':
        fileForm = FileForm(request.POST, request.FILES)
        if fileForm.is_valid():
            file = fileForm.save(commit=False)
            file.produto = product
            file.save()
            return redirect('/products/')  
    else:
        fileForm = FileForm()
    return render(request, 'produtos/NewFile.html', {'fileForm' : fileForm})

def NewSegment(request):
    """  View of new segment  """
    createSegment = SegmentForm()
    if request.method == 'POST':
        createSegment = SegmentForm(request.POST or None)
        if createSegment.is_valid():
            createSegment.save()
            return redirect('/products')
    else:
        createSegment = SegmentForm()
    context = {'createSegment' : createSegment}
    return render(request, 'produtos/NewSegment.html', context)

def NewProductTip(request):
    """  View of new product tip  """
    createTip = TipForm()
    if request.method == 'POST':
        createTip = TipForm(request.POST or None)
        if createTip.is_valid():
            createTip.save()
            return redirect('/products')
    else:
        createTip = TipForm()
    context = {'createTip' : createTip}
    return render(request, 'produtos/NewProductTip.html', context)

def NewCategory(request):
    """  View of ney categories  """
    createCategory = CategoryForm()
    if request.method == 'POST':
        createCategory = CategoryForm(request.POST or None)
        if createCategory.is_valid():
            createCategory.save()
            return redirect('/products')
    else:
        createCategory = CategoryForm()
    context = {'createCategory' : createCategory}
    return render(request, 'produtos/NewCategory.html', context)

def NewClass(request):
    """  View of new classes  """
    createClassProduct = ClassProductForm()
    if request.method == 'POST':
        createClassProduct = ClassProductForm(request.POST or None)
        if createClassProduct.is_valid():
            createClassProduct.save()
            return redirect('/products')
    else:
        createClassProduct = ClassProductForm()
    context = {'createClassProduct' : createClassProduct}
    
    return render(request, 'produtos/NewClass.html', context)

def NewCustomerProducts(request):
    """  View of new customer products  """
    createCustomerProducts = CustomerProductsForm()
    if request.method == 'POST':
        createCustomerProducts = CustomerProductsForm(request.POST, request.FILES)
        if createCustomerProducts.is_valid():
            createCustomerProducts.save()
            return redirect('products:Customer_Products')
    else:
        createCustomerProducts = CustomerProductsForm()
    context = {'createCustomerProducts' : createCustomerProducts}
    return render(request, 'produtos/NewCustomerProducts.html', context)

def ViewProduct(request, id):
    """  View of single products  """
    context = []
    items = Item.objects.all().filter(produto_id = id).order_by('-revisao')
    filesList = Arquivo.objects.all().filter(produto_id = id).order_by('-revisao')
    product = get_object_or_404(Produto, id = id)
    paginator = Paginator(filesList, 10)
    page = request.GET.get('page')
    files = paginator.get_page(page)
    context = {
        'product': product,
        'items': items,
        'files': files,
    }
    return render(request, 'produtos/Product.html', context)

def ViewSegment(request):
    """  View of segments of products  """
    segments = Segmento.objects.all().order_by('-dateCriacao')
    return render(request, 'produtos/ViewSegment.html', {'segments' : segments})

def ViewProductTip(request):
    """  View of product tipes of products  """
    productTipes = TipoProduto.objects.all().order_by('-dateCriacao')
    return render(request, 'produtos/ViewProductTip.html', {'productTipes' : productTipes})

def ViewCategory(request):
    """  View of categories of products"""
    categories = CategoriaProduto.objects.all().order_by('-dateCriacao')
    return render(request, 'produtos/ViewCategory.html', {'categories' : categories})

def ViewClass(request):
    """  View of classes """
    classes = ClasseProduto.objects.all().order_by('-dateCriacao')
    return render(request, 'produtos/ViewClass.html', {'classes' : classes})

def UpdateProduct(request, id):
    """  View of update product  """
    product = get_object_or_404(Produto, id = id)
    updateProduct = ProdutoForm(instance = product)
    if request.method == 'POST':
        updateProduct = ProdutoForm(request.POST or None, instance = product)
        if updateProduct.is_valid():
            updateProduct.save()
            return redirect('../')
        else:
            context = {'updateProduct' : updateProduct, 'product' : product}
            return render(request, 'produtos/UpdateProduct.html', context)
    else:
        context = {'updateProduct' : updateProduct, 'product' : product}
        return render(request, 'produtos/UpdateProduct.html', context)

def UpdateSegment(request, id):
    """  View of segment of product  """
    segment = get_object_or_404(Segmento, id = id)
    updateSegment = SegmentForm(instance = segment)
    if request.method == 'POST':
        updateSegment = SegmentForm(request.POST or None, instance = segment)
        if updateSegment.is_valid():
            updateSegment.save()
            return redirect('settings:Product_Settings')
        else:
            context = {'updateSegment' : updateSegment, 'segment' : segment}
            return render(request, 'produtos/UpdateSegment.html', context)
    else:
        context = {'updateSegment' : updateSegment, 'segment' : segment}
        return render(request, 'produtos/UpdateSegment.html', context)

def UpdateProductTip(request, id):
    """  View of update product tip  """
    productTip = get_object_or_404(TipoProduto, id = id)
    updateTip = TipForm(instance = productTip)
    if request.method == 'POST':
        updateTip = TipForm(request.POST or None, instance = productTip)
        if updateTip.is_valid():
            updateTip.save()
            return redirect('settings:Product_Settings')
        else:
            context = {'updateTip' : updateTip, 'productTip' : productTip}
            return render(request, 'produtos/UpdateProductTip.html', context)
    else:
        context = {'updateTip' : updateTip, 'productTip' : productTip}
        return render(request, 'produtos/UpdateProductTip.html', context)

def UpdateCategory(request, id):
    """  View of update category of product  """
    category = get_object_or_404(CategoriaProduto, id = id)
    updateCategory = CategoryForm(instance = category)
    if request.method == 'POST':
        updateCategory = CategoryForm(request.POST or None, instance = category)
        if updateCategory.is_valid():
            updateCategory.save()
            return redirect('settings:Product_Settings')
        else:
            context = {'updateCategory' : updateCategory, 'category' : category}
            return render(request, 'produtos/UpdateCategory.html', context)
    else:
        context = {'updateCategory' : updateCategory, 'category' : category}
        return render(request, 'produtos/UpdateCategory.html', context)

def UpdateClass(request, id):
    """"  View of update class of product  """
    classProduct = get_object_or_404(ClasseProduto, id = id)
    updateClassProduct = ClassProductForm(instance = classProduct)
    if request.method == 'POST':
        updateClassProduct = ClassProductForm(request.POST or None, instance = classProduct)
        if updateClassProduct.is_valid():
            updateClassProduct.save()
            return redirect('settings:Product_Settings')
        else:
            context = {'updateClassProduct' : updateClassProduct, 'classProduct' : classProduct}
            return render(request, 'produtos/UpdateClass.html', context)
    else:
        context = {'updateClassProduct' : updateClassProduct, 'classProduct' : classProduct}
        return render(request, 'produtos/UpdateClass.html', context)

def DownloadItem(request, path):
    """  View of download item  """
    filePath = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(filePath):
        with open(filePath, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/file")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filePath);
            return response
    raise Http404

def DeleteProduct(request, id):
    """  View of delete product  """
    product = get_object_or_404(Produto, id = id)
    if request.method == 'POST':
        product.delete()
        return redirect('../')
    context = {'product' : product}
    return render(request, 'produtos/DeleteProduct.html', context)

def DeleteItem(request, id):
    """  View of delete item  """
    item = get_object_or_404(Item, id = id)
    if request.method == 'POST':
        item.delete()
        return redirect('../')
    context = {'item' : item}
    return render(request, 'produtos/DeleteItem.html', context)

def DeleteFile(request, id):
    """  View of delete file  """
    file = get_object_or_404(Arquivo, id = id)
    if request.method == 'POST':
        file.delete()
        return redirect('../')
    context = {'file' : file}
    return render(request, 'produtos/DeleteFile.html', context)

def DeleteSegment(request, id):
    """
    View of delete segment
    """
    segment = get_object_or_404(Segmento, id = id)
    if request.method == 'POST':
        segment.delete()
    context = {'segment' : segment}
    return render(request, 'produtos/DeleteSegment.html', context)

def DeleteProductTip(request, id):
    """
    View of delete product tip
    """
    productTip = get_object_or_404(TipoProduto, id = id)
    if request.method == 'POST':
        productTip.delete()
    context = {'productTip' : productTip}
    return render(request, 'produtos/DeleteProductTip.html', context)

def DeleteCategory(request, id):
    """
        View of delete category product
    """
    category = get_object_or_404(CategoriaProduto, id = id)
    if request.method == 'POST':
        category.delete()
    context = {'category' : category}
    return render(request, 'produtos/DeleteCategory.html', context)

def DeleteClassProduct(request, id):
    """
    View of delete class product
    """
    classProduct = get_object_or_404(ClasseProduto, id = id)
    if request.method == 'POST':
        classProduct.delete()
    context = {'classProduct' : classProduct}
    return render(request, 'produtos/DeleteClassProduct.html', context)

def SerialNumber(request):
    """
        View of serial number main
    """
    productsList = Produto.objects.all()
    serialNumbersList = NumeroSerie.objects.all().order_by('-dateCriacao')
    paginator = Paginator(serialNumbersList, 10)
    page = request.GET.get('page')
    serialNumbers = paginator.get_page(page)
    context = {'serialNumbers' : serialNumbers, 'productsList' : productsList}
    return render(request, 'produtos/SerialNumber.html', context)

def GenerateSerial(request):
    """
        View of choice product for generate serial number
    """
    productsList = Produto.objects.all()
    generate = request.GET.get('generate')
    if generate:
        productsList = Produto.objects.filter(nome__icontains = generate)
    paginator = Paginator(productsList, 10)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {'products' : products}
    return render(request, 'produtos/NewSerialNumber.html', context)

def GenerateSerialSingle(request, id):
    """
        View of generate serial number
    """
    serialNumberForm = SerialNumberForm()
    product = Produto.objects.get(id=id)
    if request.method == 'POST':
        serialNumberForm = SerialNumberForm(request.POST or None)
        if serialNumberForm.is_valid():
            os = serialNumberForm.save(commit=False)
            os.numeroSerie = id
            os.produto = product
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
    context = {'serialNumberForm': serialNumberForm}
    return render(request, 'produtos/SerialNumberid.html', context)

def GetPartNumber(request, id):
    """
        View of partnumber generator
    """
    createPartNumber = PartNumberForm()
    file = Arquivo.objects.get(id=id)
    product = file.produto
    if request.method == 'POST':
        createPartNumber = PartNumberForm(request.POST or None)
        if createPartNumber.is_valid():
            pt = createPartNumber.save(commit=False)
            productTip = product.tipoProduto.sigla
            sldTip = file.tipoArquivo
            year=datetime.date.today().strftime("%y")
            codeNumber=file.produto.id
            if len(str(codeNumber)) == 1:
                codeNumber = '00' + str(codeNumber)
            elif len(str(codeNumber)) == 2:
                codeNumber = '0' + str(codeNumber)
            else:
                codeNumber = codeNumber
            review=file.revisao
            if len(str(review)) < 2:
                review = '0' + str(review)
            check=PartNumber.objects.filter(produto=product).exists()
            if check == True:
                partnumber=PartNumber.objects.filter(produto=product).last()
                var=int(partnumber.partNumber[13:])
                var+=1
            else:
                var=100
            pt.partNumber=str(productTip) + str(sldTip) + '-' + str(codeNumber) + '-' + str(year) + str(review) + '-' + str(var)
            pt.produto=product
            pt.save()
            file.partNumber_id = pt.id
            file.save()
            
            return redirect('../')
    context={'createPartNumber':createPartNumber}
    return render(request, 'produtos/NewPartNumber.html', context)

def CustomerProducts(request):
    """
        View of products of customer
    """
    customerProductsList = ProdutoCliente.objects.all()
    paginator = Paginator(customerProductsList, 10)
    page = request.GET.get('page')
    customerProducts = paginator.get_page(page)
    
    context = {'customerProducts' : customerProducts}
    return render(request, 'produtos/CustomerProducts.html', context)