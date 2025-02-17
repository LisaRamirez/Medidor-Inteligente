from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.http import HttpResponse

# Create your views here.

def home(request):
    
    return render(request, 'app/home.html')

def clientes(request):
    return render(request, 'app/clientes.html')


def nosotros(request):
    return render(request, 'app/nosotros.html')

def recursos(request):
    return render(request, 'app/recursos.html')

def soluciones(request):
    return render(request, 'app/soluciones.html')

def contacto(request):

    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST['telefono']
        apr = request.POST['apr']
        cargo = request.POST['cargo']
        comuna = request.POST['comuna']
        arranque = request.POST['arranque']
        financiamiento = request.POST['financiamiento']
        mensaje = request.POST['mensaje']

      


    return render(request, 'app/contacto.html')
