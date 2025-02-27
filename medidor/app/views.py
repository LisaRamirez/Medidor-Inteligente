import datetime
import smtplib
import os
from django.http import Http404
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
from django.http import JsonResponse

def mi_vista(request):
    return render(request, 'recursos.html', {'MEDIA_URL': settings.MEDIA_URL})
# Create your views here.


def clientes(request):
    try:
        appr = Apr.objects.all()
        data = {    
            'apr': appr
        }
    except Exception as e:
            print(f"Unexpected error: {e}")
            messages.error(request, 'Hubo un problema con tu solicitud.')
            return redirect('app/e404.html')
    return render(request, 'app/clientes.html',data)

def filtrar_apr(request):
    try:
        region = request.GET.get('region')  # Obtiene la región desde el GET
        if region:
            aprs = Apr.objects.filter(region__iexact=region).values('id', 'nameapr', 'comuna', 'region', 'imagen')
            return JsonResponse(list(aprs), safe=False)  # Retorna JSON con los datos filtrados
    except Exception as e:
            print(f"Unexpected error: {e}")
            messages.error(request, 'Hubo un problema con tu solicitud.')
            return redirect('app/e404.html')    
    return JsonResponse([], safe=False)






def apr(request, apr_id):
    try:
        apppr = get_object_or_404(Apr, id=apr_id)
        data = {    
            'appr': apppr,

        }
    except data.DoesNotExist:
        return redirect('app/e404.html')
    return render(request, 'app/apr.html',data)

def home(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            ssr_apr = request.POST['ssr_apr']
            cargo_apr = request.POST['cargo_apr']
            comuna = request.POST['comuna']
            cantidad = request.POST['cantidad']
            fecha = datetime.datetime.now()
            radio = request.POST['financiamiento']
            message = request.POST['message']   

            contacto = Contacto(name=name, email=email, phone=phone, ssr_apr=ssr_apr, cargo_apr=cargo_apr, comuna=comuna, cantidad=cantidad, fecha=fecha, radio=radio, message=message)
            contacto.save()
            inicio = settings.EMAIL_HOST_USER
            password = settings.EMAIL_HOST_PASSWORD
            info = f"nombre: {name} \n phone: {phone} \n ssr_apr: {ssr_apr} \n cargo_apr: {cargo_apr} \n comuna: {comuna} \n cantidad: {cantidad} \n fecha: {fecha} \n radio: {radio} \n message: {message}"
            cc_recipients =['','']
            try:
                send_email('APR/SSR contacto', info, inicio, password, email, cc_recipients, 'smtp.gmail.com', 587)
                messages.success(request, 'Tu mensaje ha sido enviado correctamente')
            except send_email.error as e:
                print(f"Error: Email could not be sent. {e}")   
    except Exception as e:
        print(f"Unexpected error: {e}")
        messages.error(request, 'Hubo un problema con tu solicitud.')
        return redirect('app/e404.html')  # Change to an appropriate error page

    return render(request, 'app/home.html')


def contacto(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            ssr_apr = request.POST['ssr_apr']
            cargo_apr = request.POST['cargo_apr']
            comuna = request.POST['comuna']
            cantidad = request.POST['cantidad']
            fecha = datetime.datetime.now()
            radio = request.POST['financiamiento']
            message = request.POST['message']   

            contacto = Contacto(name=name, email=email, phone=phone, ssr_apr=ssr_apr, cargo_apr=cargo_apr, comuna=comuna, cantidad=cantidad, fecha=fecha, radio=radio, message=message)
            contacto.save()
            inicio = settings.EMAIL_HOST_USER
            password = settings.EMAIL_HOST_PASSWORD
            info = f"nombre: {name} \n phone: {phone} \n ssr_apr: {ssr_apr} \n cargo_apr: {cargo_apr} \n comuna: {comuna} \n cantidad: {cantidad} \n fecha: {fecha} \n radio: {radio} \n message: {message}"
            cc_recipients =['cristobalfariasfredes@gmail.com','']
            try:
                send_email('APR/SSR contacto', info, inicio, password, email, cc_recipients, 'smtp.gmail.com', 587)
                messages.success(request, 'Tu mensaje ha sido enviado correctamente')
            except send_email.error as e:
                print(f"Error: Email could not be sent. {e}")
            raise Http404   
    except Exception as e:
            print(f"Unexpected error: {e}")
            messages.error(request, 'Hubo un problema con tu solicitud.')
            

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




def nosotros(request):
    return render(request, 'app/nosotros.html')




def recursos(request):
    return render(request, 'app/recursos.html')

def soluciones(request):
    return render(request, 'app/soluciones.html')

def e404(request):
    return render(request, 'app/e404.html')

def prueba(request):
    
   
    
    return render(request, 'app/prueba.html')
