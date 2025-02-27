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


from django.core.mail import EmailMultiAlternatives

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
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            ssr_apr = request.POST.get('ssr_apr', '')
            cargo_apr = request.POST.get('cargo_apr', '')
            comuna = request.POST.get('comuna', '')
            cantidad = request.POST.get('cantidad', '')
            radio = request.POST.get('financiamiento', '')
            message = request.POST.get('message', '')
            fecha = datetime.now()

            # Guardar en la base de datos
            contacto = Contacto(
                name=name, email=email, phone=phone, ssr_apr=ssr_apr, 
                cargo_apr=cargo_apr, comuna=comuna, cantidad=cantidad, 
                fecha=fecha, radio=radio, message=message
            )
            contacto.save()

            # Enviar correo
            sender_email = settings.EMAIL_HOST_USER
            password = settings.EMAIL_HOST_PASSWORD
            smtp_server = settings.EMAIL_HOST
            smtp_port = settings.EMAIL_PORT

            info = (f"Nombre: {name}\nTeléfono: {phone}\nSSR/APR: {ssr_apr}\n"
                    f"Cargo APR: {cargo_apr}\nComuna: {comuna}\nCantidad: {cantidad}\n"
                    f"Fecha: {fecha}\nFinanciamiento: {radio}\nMensaje: {message}")

            cc_emails = ['cristobalfariasfredes@gmail.com', 'lisaisabelc19@gmail.com']
            subject = 'APR/SSR Contacto'

            send_email(subject, info, sender_email, password, email, cc_emails, smtp_server, smtp_port)

            messages.success(request, 'Tu mensaje ha sido enviado correctamente')
            return redirect('home')  # Redirige a la vista principal después de enviar

        except Exception as e:
            print(f"Error: {e}")
            messages.error(request, 'Hubo un error al procesar tu solicitud. Inténtalo nuevamente.')
            return redirect('error_page')  # Cambiar por una vista de error adecuada

    return render(request, 'app/home.html')



def contacto(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            ssr_apr = request.POST.get('ssr_apr', '')
            cargo_apr = request.POST.get('cargo_apr', '')
            comuna = request.POST.get('comuna', '')
            cantidad = request.POST.get('cantidad', '')
            radio = request.POST.get('financiamiento', '')
            message = request.POST.get('message', '')
            fecha = datetime.now()

            # Guardar en la base de datos
            contacto = Contacto(
                name=name, email=email, phone=phone, ssr_apr=ssr_apr, 
                cargo_apr=cargo_apr, comuna=comuna, cantidad=cantidad, 
                fecha=fecha, radio=radio, message=message
            )
            contacto.save()

            # Enviar correo
            sender_email = settings.EMAIL_HOST_USER
            password = settings.EMAIL_HOST_PASSWORD
            smtp_server = settings.EMAIL_HOST
            smtp_port = settings.EMAIL_PORT

            info = (
                    f"Estimado/a {name},\n\n"
                    f"Agradecemos sinceramente tu solicitud. A continuación, te detallamos la información recibida:\n\n"
                    f"Datos Personales:\n"
                    f"• Nombre: {name}\n"
                    f"• Teléfono: {phone}\n"
                    f"• Comuna: {comuna}\n\n"
                    f"Detalles de SSR Y APR:\n"
                    f"• SSR/APR: {ssr_apr}\n"
                    f"• Cargo APR: {cargo_apr}\n"
                    f"• Cantidad: {cantidad}\n"
                    f"• Fecha: {fecha}\n\n"
                    f"Información de Financiamiento:\n"
                    f"• Financiamiento: {radio}\n\n"
                    f"Mensaje: {message}\n\n"
                    f"Quedamos a tu disposición para cualquier consulta adicional.\n\n"
                    f"Atentamente, {name}. \n"
                    f"El equipo de atención al cliente de Medidor Inteligente.")

            cc_emails = ['', 'contacto@medidorinteligente.cl']
            subject = 'APR/SSR Contacto'

            send_email(subject, info, sender_email, password, email, cc_emails, smtp_server, smtp_port)

            messages.success(request, 'Tu mensaje ha sido enviado correctamente')
            return redirect('contacto')  # Redirigir a la página de contacto o donde corresponda

        except Exception as e:
            print(f"Error: {e}")
            messages.error(request, 'Hubo un error al enviar el mensaje. Inténtalo nuevamente.')
            return redirect('error_page')  # Cambiar por una vista de error apropiada

    return render(request, 'app/contacto.html')
    
    

def send_email(subject, info, sender_email, password, recipient_email,cc_emails, smtp_server, smtp_port):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        msg = MIMEText(info)
        msg['Subject'] = subject
        msg['From'] = sender_email
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
