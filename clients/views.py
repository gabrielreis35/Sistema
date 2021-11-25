from django.shortcuts import redirect, render

from clients.forms import ClientForm
from .models import Cliente

def HomeClients(request):
    clients = Cliente.objects.all().order_by('-dateCriacao')
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