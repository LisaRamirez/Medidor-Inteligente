import logging
import datetime
import smtplib
import os
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.http import HttpResponse
from .models import Contacto, Apr
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseServerError
from django.http import HttpResponseNotFound
from smtplib import SMTPException
from django.http import JsonResponse
from datetime import datetime
from django.core.mail import EmailMultiAlternatives




def mi_vista(request):
    return render(request, 'recursos.html', {'MEDIA_URL': settings.MEDIA_URL})
# Create your views here.

logger = logging.getLogger(__name__)
logger = logging.getLogger('django')

def clientes(request):
    try:
        # Validación de parámetros inesperados en la URL
        if request.GET or request.POST:
            messages.error(request, 'Parámetros no permitidos en la solicitud.')
            return redirect('app/error_404')  # Redirige a la página de error
        
        # Obtener todos los objetos de Apr
        appr = Apr.objects.all()
        data = {'apr': appr}
        
        return render(request, 'app/clientes.html', data)

    except Exception as e:
        print(f"Unexpected error: {e}")
        messages.error(request, 'Hubo un problema con tu solicitud.')
        return redirect('app/error_404')  # Redirige a la página de error




def filtrar_apr(request):
    try:
        # Verificar si hay parámetros GET inesperados
        if not request.GET.get('region'):
            messages.error(request, 'Parámetros no permitidos o faltantes en la solicitud.')
            return redirect('app/error_404')  # Redirige a la página de error

        # Obtener la región del parámetro GET
        region = request.GET.get('region')
        
        # Filtrar los registros por región (ignorando mayúsculas/minúsculas)
        aprs = Apr.objects.filter(region__iexact=region).values(
            'id', 'nameapr', 'comuna', 'region', 'imagen'
        )
        
        # Retornar JSON con los datos filtrados
        return JsonResponse(list(aprs), safe=False)

    except Exception as e:
        print(f"Unexpected error: {e}")
        messages.error(request, 'Hubo un problema con tu solicitud.')
        return redirect('app/error_404')  # Redirige a la página de error








def apr(request, apr_id):
    try:
        apppr = get_object_or_404(Apr, id=apr_id)  # get_object_or_404 ya maneja errores
        data = {'appr': apppr}
        return render(request, 'app/apr.html', data)
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        messages.error(request, 'Hubo un problema al cargar la información.')
        return redirect('app/error_404')  # Redirige a una página de error




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
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

            cc_emails = ['cristobalfariasfredes@gmail.com', 'lisaisabelc19@gmail.com']
            subject = 'APR/SSR Contacto'

            send_email(subject, info, sender_email, password, email, cc_emails, smtp_server, smtp_port)

            messages.success(request, 'Tu mensaje ha sido enviado correctamente')
            return redirect('home')  # Redirige a la vista principal después de enviar

        except Exception as e:
            print(f"Error: {e}")
            messages.error(request, 'Hubo un error al procesar tu solicitud. Inténtalo nuevamente.')
            return redirect('app/error_404')  # Cambiar por una vista de error adecuada

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

            cc_emails = ['cristobalfariasfredes@gmail.com', 'lisaisabelc19@gmail.com']
            subject = 'APR/SSR Contacto'

            send_email(subject, info, sender_email, password, email, cc_emails, smtp_server, smtp_port)

            messages.success(request, 'Tu mensaje ha sido enviado correctamente')
            return redirect('contacto')  # Redirigir a la página de contacto o donde corresponda

        except Exception as e:
            print(f"Error: {e}")
            messages.error(request, 'Hubo un error al enviar el mensaje. Inténtalo nuevamente.')
            return redirect('app/error_404')  # Cambiar por una vista de error apropiada

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
    try:
        return render(request, 'app/nosotros.html')
    except Exception as e:
        logger.error(f"Error al renderizar la página: {e}", exc_info=True)
        return HttpResponseServerError("Hubo un error al cargar la página. Inténtalo más tarde.")




def soluciones(request):
    try:
        return render(request, 'app/soluciones.html')
    except Exception as e:
        logger.error(f"Error al renderizar la página: {e}", exc_info=True)
        return HttpResponseServerError("Hubo un error al cargar la página. Inténtalo más tarde.")

def recursos(request):
    try:
        return render(request, 'app/recursos.html')
    except Exception as e:
        logger.error(f"Error al renderizar la página: {e}", exc_info=True)
        return HttpResponseServerError("Hubo un error al cargar la página. Inténtalo más tarde.")

def error_404(request, exception=None):
    try:
        return render(request, 'app/error_404', status=404)
    except Exception as e:
        logger.error(f"Error al renderizar la página 404: {e}", exc_info=True)
        return HttpResponseNotFound("Página no encontrada, pero ocurrió un error al cargar la plantilla.")

def prueba(request):
    try:
        return render(request, 'app/prueba.html')
    except Exception as e:
        logger.error(f"Error al renderizar la página: {e}", exc_info=True)
        return HttpResponseServerError("Hubo un error al cargar la página. Inténtalo nuevamente más tarde.")




def test_logging():
    logger.info("Este es un mensaje informativo.")
    logger.warning("Advertencia: Algo podría estar mal.")
    logger.error("Error: Algo falló.")
    logger.critical("¡Error crítico!")