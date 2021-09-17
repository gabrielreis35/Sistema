from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404

def Users(request):
    return render(request, 'users.html')