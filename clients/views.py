from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from clients.forms import ClientForm
from .models import Cliente

def HomeClients(request):
    search = request.GET.get('search')
    
    if search:
        clientsList = Cliente.objects.filter(nome__icontains = search)
        paginator = Paginator(clientsList, 10)
        page = request.GET.get('page')
        clients = paginator.get_page(page)
    else:    
        clientsList = Cliente.objects.all().order_by('-dateCriacao')
        paginator = Paginator(clientsList, 10)
        page = request.GET.get('page')
        clients = paginator.get_page(page)
    context = {'clients' : clients }
    return render(request, 'clients/HomeClients.html', context)

def NewClient(request):
    createClient = ClientForm()
    if request.method == 'POST':
        createClient = ClientForm(request.POST or None)
        if createClient.is_valid():
            createClient.save()
            return redirect('../../')
        
    else:
        createClient = ClientForm()
    
    context = {
        'createClient' : createClient
    }
            
    return render(request, 'clients/NewClient.html', context)