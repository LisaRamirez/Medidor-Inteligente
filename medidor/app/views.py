import smtplib
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.http import HttpResponse
from .models import Contacto, Apr
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from smtplib import SMTPException

# Create your views here.
def contacto(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        ssr_apr = request.POST['ssr_apr']
        cargo_apr = request.POST['cargo_apr']
        comuna = request.POST['comuna']
        cantidad = request.POST['cantidad']
        fecha = request.POST['fecha']
        radio = request.POST['financiamiento']
        mensaje = request.POST['mensaje']

       
        contacto = Contacto(name=name, email=email, phone=phone, ssr_apr=ssr_apr, cargo_apr=cargo_apr, comuna=comuna, cantidad=cantidad, fecha=fecha, radio=radio, mensaje=mensaje)
        contacto.save()
        inicio = settings.EMAIL_HOST_USER
        password = settings.EMAIL_HOST_PASSWORD
        info = f"nombre: {name} \n phone: {phone} \n ssr_apr: {ssr_apr} \n cargo_apr: {cargo_apr} \n comuna: {comuna} \n cantidad: {cantidad} \n fecha: {fecha} \n radio: {radio} \n mensaje: {mensaje}"
        cc_recipients =['cristobalfariasfredes@gmail.com','lisaisabelc19@gmail.com']

        send_email('APR/SSR contacto', info, inicio, password, email, cc_recipients, 'smtp.gmail.com', 587)

    return render(request, 'app/contacto.html')

def send_email(subject, message, sender_email, sender_password, recipient_email,cc_emails, smtp_server, smtp_port):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Cc'] = ', '.join(cc_emails)  # Agregar los correos de CC
        all_recipients = [recipient_email] + cc_emails
        server.sendmail(sender_email, all_recipients, msg.as_string())
        server.quit()
        print('Email sent successfully!')
    except smtplib.SMTPException as e:
        print(f"Error: Email could not be sent. {e}")


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

def apr(request):
    return render(request, 'app/apr.html')


