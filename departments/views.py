from django.contrib.auth.decorators import login_required
from departments.forms import DepartmentForm
from django.shortcuts import redirect, render
from .models import Departamento

def HomeDepartment(request):
    departments = Departamento.objects.all()
    context = {'departments' : departments}
    return render(request, 'departments/Departments.html', context)

def CreateDepartment(request):
    createDepartment = DepartmentForm()
    
    if request.method == 'POST':
        createDepartment = DepartmentForm(request.POST or None)
        if createDepartment.is_valid():
            createDepartment.save()
            return redirect('../')
    else:
        createDepartment = DepartmentForm()
    
    context = {'createDepartment': createDepartment}
    return render(request, 'departments/NewDepartment.html', context)