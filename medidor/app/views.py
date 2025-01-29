from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def clientes(request):
    return render(request, 'app/clientes.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')

def recursos(request):
    return render(request, 'app/recursos.html')

def soluciones(request):
    return render(request, 'app/soluciones.html')

