from django.shortcuts import render

def Home(request):
    return render(request, 'main/Home.html')

def Login(request):
    return render(request, 'main/Login.html')