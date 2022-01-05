from django.contrib.auth.decorators import login_required
from departments.forms import DepartmentForm
from django.shortcuts import get_object_or_404, redirect, render

from produtos.views import DeleteClassProduct
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
            return redirect('departments:New_Department')
    else:
        createDepartment = DepartmentForm()
    
    context = {'createDepartment': createDepartment}
    return render(request, 'departments/NewDepartment.html', context)

def DeleteDepartment(request, id):
    department = get_object_or_404(Departamento, id=id)
    if request.method == "POST":
        department.delete()
        return redirect("departments:Home_Departments")
    context = {'department':department}
    return render(request, 'departments/DeleteDepartment.html', context)