from django.shortcuts import render

def Departments(request):
    return render(request, 'departments.html')