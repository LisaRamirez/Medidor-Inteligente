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
from datetime import datetime

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
            fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            radio = request.POST['financiamiento']
            message = request.POST['message']   

            # Save the data in the Contacto model
            contacto = Contacto(name=name, email=email, phone=phone, ssr_apr=ssr_apr, cargo_apr=cargo_apr, comuna=comuna, cantidad=cantidad, fecha=fecha, radio=radio, message=message)
            contacto.save()

            # Send email with the form data
            inicio = settings.EMAIL_HOST_USER
            password = settings.EMAIL_HOST_PASSWORD
            smtp = settings.EMAIL_HOST
            cc_emails = ['lisaisabelc19@gmail.com']  # You can add more here

            try:
                send_email(
                    subject="Nuevo Mensaje de Contacto",
                    message=message,
                    sender_email=inicio,
                    sender_password=password,
                    recipient_email=email,
                    cc_emails=cc_emails,
                    smtp_server= smtp,  # Replace with actual SMTP server
                    smtp_port=587,
                    name=name,
                    phone=phone,
                    ssr_apr=ssr_apr,
                    cargo_apr=cargo_apr,
                    comuna=comuna,
                    cantidad=cantidad,
                    fecha=fecha,
                    radio=radio
                )
                messages.success(request, 'Tu mensaje ha sido enviado correctamente.')
            except smtplib.SMTPException as e:
                print(f"❌ Error: No se pudo enviar el email. {e}")
                messages.error(request, 'Hubo un problema al enviar el correo. Intenta de nuevo.')

            return render(request, 'app/contacto.html')  # Or redirect to a thank-you page, if needed

    except Exception as e:
        print(f"Unexpected error: {e}")
        messages.error(request, 'Hubo un problema con tu solicitud.')

    return render(request, 'app/contacto.html')

def send_email(subject, message, sender_email, sender_password, recipient_email, cc_emails, smtp_server, smtp_port, name, phone, ssr_apr, cargo_apr, comuna, cantidad, fecha, radio):
    try:
        # Configurar servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)

        # Crear el correo en formato HTML
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Cc'] = ', '.join(cc_emails)  # Agregar CC
        all_recipients = [recipient_email] + cc_emails

        # Estilizar el mensaje HTML
        html_message = f"""
         <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <h2 style="color: #2C3E50;">Nuevo Mensaje de Contacto</h2>
                <table border="1" cellspacing="0" cellpadding="8" style="border-collapse: collapse; width: 100%;">
                    <tr><th style="background: #f2f2f2; text-align: left;">Nombre</th><td>{name}</td></tr>
                    <tr><th style="background: #f2f2f2; text-align: left;">Teléfono</th><td>{phone}</td></tr>
                    <tr><th style="background: #f2f2f2; text-align: left;">SSR/APR</th><td>{ssr_apr}</td></tr>
                    <tr><th style="background: #f2f2f2; text-align: left;">Cargo APR</th><td>{cargo_apr}</td></tr>
                    <tr><th style="background: #f2f2f2; text-align: left;">Comuna</th><td>{comuna}</td></tr>
                    <tr><th style="background: #f2f2f2; text-align: left;">Cantidad</th><td>{cantidad}</td></tr>
                    <tr><th style="background: #f2f2f2; text-align: left;">Fecha</th><td>{fecha}</td></tr>
                    <tr><th style="background: #f2f2f2; text-align: left;">Financiamiento</th><td>{radio}</td></tr>
                    <tr><th style="background: #f2f2f2; text-align: left;">Mensaje</th><td>{message}</td></tr>
                </table>
                <p style="margin-top: 20px;">Este mensaje fue enviado desde el formulario de contacto.</p>
            </body>
            </html>
            """

        # Agregar HTML como parte del correo
        msg.attach(MIMEText(html_message, "html"))

        # Enviar correo
        server.sendmail(sender_email, all_recipients, msg.as_string())
        server.quit()
        print('✅ Email enviado correctamente!')
    except smtplib.SMTPException as e:
        print(f"❌ Error: No se pudo enviar el email. {e}")
        messages.error('Hubo un problema al enviar el correo. Intenta de nuevo.')






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
