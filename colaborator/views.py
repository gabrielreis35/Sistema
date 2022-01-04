from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from colaborator.models import Colaborador

@login_required
def ColaboratorView(request):
    search = request.GET.get('search')
    colaboratorsList = Colaborador.objects.all().order_by('-dateCriacao')
    
    if search:
        colaboratorsList = Colaborador.objects.filter(nome__icontains = search)
    
    paginator = Paginator(colaboratorsList, 10)
    page = request.GET.get('page')
    colaborators = paginator.get_page(page)
    
    context = {
        'colaborators' : colaborators
    }
    return render(request, 'colaborator/User.html', context) 

@login_required
def ColaboratorRegister(request):
    if request.method == 'POST':
        name = request.POST['nome']
        lastName = request.POST['sobrenome']
        email = request.POST['email']
        confirmEmail = request.POST['email2']
        password = request.POST['password']
        password2 = request.POST['password2']
    
        if not name.strip():
            return 0
        if not lastName.strip():
            return 0
        if not email.strip():
            return 0
        if email != confirmEmail:
            return 0
        if User.objects.filter(email=email).exists():
            return 0
        user = User.objects.create_user(username=name, first_name=name, last_name=lastName, email=email, password=password)
        user.save()
    
    return render(request, 'colaborator/Signup.html')