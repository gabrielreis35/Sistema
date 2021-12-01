from django.contrib.auth import login
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from produtos.models import Produto, TipoProduto

from .models import Informacoes
# from django.contrib import messages

@login_required
def Home(request):
    countProduct = Produto.objects.count()
    acessorio = Produto.objects.filter(tipoProduto__nome = 'Acessório').count()
    carregadeira = Produto.objects.filter(tipoProduto__nome = 'Carregadeira').count()
    chapaDesgaste = Produto.objects.filter(tipoProduto__nome = 'Chapa de desgaste').count()
    chockBar = Produto.objects.filter(tipoProduto__nome = 'Chock bar').count()
    dispFer = Produto.objects.filter(tipoProduto__nome = 'Dispositivos e ferramentas').count()
    engate = Produto.objects.filter(tipoProduto__nome = 'Engate rápido').count()
    escavadeira = Produto.objects.filter(tipoProduto__nome = 'Escavadeira').count()
    ferramentaSolo = Produto.objects.filter(tipoProduto__nome = 'Ferramenta de penetração de solo').count()
    garfo = Produto.objects.filter(tipoProduto__nome = 'Garfo').count()
    graniteira = Produto.objects.filter(tipoProduto__nome = 'Graniteira').count()
    lamina = Produto.objects.filter(tipoProduto__nome = 'Lâmina').count()
    lanca = Produto.objects.filter(tipoProduto__nome = 'Lança').count()
    ripper = Produto.objects.filter(tipoProduto__nome = 'Ripper').count()
    segmento = Produto.objects.filter(tipoProduto__nome = 'Segmento').count()
    vala = Produto.objects.filter(tipoProduto__nome = 'Vala').count()
    servico = Produto.objects.filter(tipoProduto__nome = 'Serviço').count()
    
    context = {
        'countProduct' : countProduct,
        'acessorio' : acessorio,
        'carregadeira' : carregadeira,
        'chapaDesgaste' : chapaDesgaste,
        'chockBar' : chockBar,
        'graniteira' : graniteira,
        'dispFer' : dispFer,
        'engate' : engate,
        'escavadeira' : escavadeira,
        'ferramentaSolo' : ferramentaSolo,
        'garfo' : garfo,
        'lamina' : lamina,
        'lanca' : lanca,
        'ripper' : ripper,
        'segmento' : segmento,
        'vala' : vala,
        'servico' : servico
    }
    return render(request, 'main/Home.html', context)