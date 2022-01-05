from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from colaborator.models import Colaborador
from departments.models import Departamento

@login_required
def ColaboratorView(request):
    search = request.GET.get('search')
    colaboratorsList = User.objects.all()
    
    if search:
        colaboratorsList = User.objects.filter(name__icontains = search)
    
    paginator = Paginator(colaboratorsList, 10)
    page = request.GET.get('page')
    colaborators = paginator.get_page(page)
    
    context = {
        'colaborators' : colaborators
    }
    return render(request, 'colaborator/User.html', context) 

@login_required
def ColaboratorRegister(request):
    departments = Departamento.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        office = request.POST['office']
        department = request.POST['department']
        email = request.POST['email']
        confirmEmail = request.POST['email2']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not name.strip():
            messages.error(request, "Nome não pode estar vazio.")
            return redirect('colaborators:Signup_Colaborator')
        if not lastname.strip():
            messages.error(request, "Sobrenome não pode estar vazio.")
            return redirect('colaborators:Signup_Colaborator')
        if not office.strip():
            messages.error(request, "Cargo não pode estar vazio")
            return redirect('colaborators:Signup_Colaborator')
        if not department.strip():
            messages.error(request, "Departamento não pode estar vazio")
            return redirect('colaborators:Signup_Colaborator')
        if not email.strip():
            messages.error(request, "Email não pode estar vazio.")
            return redirect('colaborators:Signup_Colaborator')
        if email != confirmEmail:
            messages.error("Email diferentes, favor colocar email iguais.")
            return redirect('colaborators:Signup_Colaborator')
        if password != password2:
            messages.error(request, "Senhas diferentes.")
            return redirect('colaborators:Signup_Colaborator')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Usuário já cadastrado")
            return redirect('colaborators:Signup_Colaborator')
        if User.objects.filter(username=name).exists():
            messages.error(request, "Usuário já cadastrado")
            return redirect('colaborators:Signup_Colaborator')
        # try:
        #     setDepartment = Departamento.objects.get(id=int(department))
        # except Departamento.DoesNotExist:
        #     setDepartment = None
        user = User.objects.create_user(username=name, first_name=name, last_name=lastname, email=email, password=password)
        user.save()
        # try:
        #     setUser = int(user.id)
        # except:
        #     setUser = None
        # colaborator = Colaborador(nome=name+" "+lastname, departamento=setDepartment, cargo=office, email=email, user=setUser)
        # print(colaborator)
        # colaborator.save()
    context = {
        'departments': departments
    }
    return render(request, 'colaborator/Signup.html', context)