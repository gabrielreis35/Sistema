from django.http import request
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from produtos.models import Segmento, TipoProduto
from .models import ConfiguracoesProduto

def Settings(request):
    return render(request, 'settings/Settings.html')

def ProductSettings(request):
    settingsSegmentsList = Segmento.objects.all().order_by('-dateCriacao')
    settingsTipProducts = TipoProduto.objects.all().order_by('-dateCriacao')
    
    paginator = Paginator(settingsSegmentsList, 5)
    page = request.GET.get('page')
    settingsSegments = paginator.get_page(page)
    
    context = {
        'settingsSegments': settingsSegments,
        'settingsTipProducts': settingsTipProducts
    }
    return render(request, 'settings/ProductSettings.html', context)