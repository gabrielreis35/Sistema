from django.db.models.query import EmptyQuerySet
from django.http import request
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from produtos.models import CategoriaProduto, ClasseProduto, Segmento, TipoProduto
from workOrder.models import OrdemServico
def Settings(request):
    return render(request, 'settings/Settings.html')

def ProductSettings(request):
    settingsSegmentsList = Segmento.objects.all().order_by('-dateCriacao')
    paginator = Paginator(settingsSegmentsList, 5)
    page = request.GET.get('page1')
    try:
        settingsSegments = paginator.get_page(page)
    except PageNotAnInteger:
        settingsSegments = paginator.page(1)
    except EmptyPage:
        settingsSegments = paginator.page(paginator.num_pages)
    
    settingsTipProductsList = TipoProduto.objects.all().order_by('-dateCriacao')
    paginator = Paginator(settingsTipProductsList, 5)
    page = request.GET.get('page2')
    try:
        settingsTipProducts = paginator.get_page(page)
    except PageNotAnInteger:
        settingsTipProducts = paginator.page(1)
    except EmptyPage:
        settingsTipProducts = paginator.page(paginator.num_pages)
    
    settingsCategoriesList = CategoriaProduto.objects.all().order_by('-dateCriacao')
    paginator = Paginator(settingsCategoriesList, 5)
    page = request.GET.get('page3')
    try:
        settingsCategories = paginator.get_page(page)
    except PageNotAnInteger:
        settingsCategories = paginator.page(1)
    except EmptyPage:
        settingsCategories = paginator.page(paginator.num_pages)
    
    settingsClassesList = ClasseProduto.objects.all().order_by('-dateCriacao')
    paginator = Paginator(settingsClassesList, 5)
    page = request.GET.get('page4')
    try:
        settingsClasses = paginator.get_page(page)
    except PageNotAnInteger:
        settingsClasses = paginator.page(1)
    except EmptyPage:
        settingsClasses = paginator.page(paginator.num_pages)

    context = {
        'settingsSegments': settingsSegments,
        'settingsTipProducts': settingsTipProducts,
        'settingsCategories': settingsCategories,
        'settingsClasses': settingsClasses
    }
    return render(request, 'settings/ProductSettings.html', context)

def WorkOrderSettings(request):
    workOrdersList = OrdemServico.objects.all().order_by('-dateCriacao')
    paginator = Paginator(workOrdersList, 10)
    page = request.GET.get('page')
    workOrders = paginator.get_page(page)
    context = {
        'workOrders': workOrders
    }
    return render(request, 'settings/WorkOrderSettings.html', context)