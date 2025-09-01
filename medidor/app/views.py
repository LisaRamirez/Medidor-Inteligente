import json
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
from .models import Contacto, Apr, Testimonio, ImagenTestimonio
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseServerError
from django.http import HttpResponseNotFound
from smtplib import SMTPException
from django.http import JsonResponse
from datetime import datetime
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect
# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .services import obtener_respuesta

def asistente_virtual(request):
    if request.method == "POST":
        pregunta = request.POST.get("pregunta", "").strip()
        if not pregunta:
            return JsonResponse({"respuesta": "No se envió ninguna pregunta."})
        respuesta = obtener_respuesta(pregunta)
        return JsonResponse({"respuesta": respuesta})
    return render(request, "app/asistente.html")


def home(request):
    return render(request, 'app/base.html')

# Otras vistas que tengas...
def home(request):
    return render(request, 'app/base.html')

def otra_vista(request):
    return render(request, 'app/otra_template.html')

def testimonio(request):
    try:
        tes = Testimonio.objects.filter(activo=True)
        imag = ImagenTestimonio.objects.all()
        data = {
            'testi' : tes,
            'imagenes': imag
        }
        return render(request, 'app/testimonio.html',data)
    except Exception as e:
        logger.error(f"Error al renderizar la página: {e}", exc_info=True)
        return HttpResponseServerError("Hubo un error al cargar la página. Inténtalo nuevamente más tarde.")

def cargar_mas_testimonios(request):
    """API para cargar más testimonios"""
    try:
        offset = int(request.GET.get('offset', 4))
        limit = int(request.GET.get('limit', 2))
        
        testimonios = Testimonio.objects.filter(activo=True)[offset:offset+limit]
        
        testimonios_data = []
        for testimonio in testimonios:
            imagenes = []
            for imagen in testimonio.imagenes.all():
                imagenes.append({
                    'url': imagen.imagen.url,
                    'alt': imagen.alt_text
                })
            
            testimonios_data.append({
                'id': testimonio.id,
                'fecha': testimonio.fecha.strftime('%d %b %Y'),
                'creador': testimonio.creador,
                'titulo': testimonio.titulo,
                'sub_titulo': testimonio.sub_titulo,
                'contenido': testimonio.contenido,
                'descripcion': testimonio.descripcion,
                'id_yt': testimonio.id_yt,
                'likes': testimonio.likes,
                'imagenes': imagenes
            })
        
        return JsonResponse({
            'success': True,
            'testimonios': testimonios_data,
            'has_more': Testimonio.objects.filter(activo=True).count() > offset + limit
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


def prueba(request):
    try:
        return render(request, 'app/testimonio.html')
    except Exception as e:
        logger.error(f"Error al renderizar la página: {e}", exc_info=True)
        return HttpResponseServerError("Hubo un error al cargar la página. Inténtalo nuevamente más tarde.")

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
            correo = request.POST.get('correo2', '')
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
                name=name, correo=correo, phone=phone, ssr_apr=ssr_apr, 
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
                    f"Datos Personales:\n"
                    f"• Nombre: {name}\n"
                    f"• Teléfono: {phone}\n"
                    f"• Comuna: {comuna}\n"
                    f"• Correo: {correo}\n\n"

                    f"Detalles de SSR Y APR:\n"
                    f"• SSR/APR: {ssr_apr}\n"
                    f"• Cargo APR: {cargo_apr}\n"
                    f"• Cantidad Arranques: {cantidad}\n"                   
                    f"• Financiamiento: {radio}\n\n"
                    f"Mensaje: {message}\n\n"
                    
                    
                    f"Página web Medidor Inteligente.")

            subject = 'Medidor Inteligente APR/SSR Contacto'
            email = "lisaisabelc19@gmail.com"
            cc_emails = [correo]
            send_email(subject, info, sender_email, password, email, cc_emails, smtp_server, smtp_port)
            return redirect('home')  # Redirige a la vista principal después de enviar

        except Exception as e:
            return render(request, 'app/e404.html', {'error': str(e)})  # Cambiar por una vista de error apropiad

    return render(request, 'app/home.html')

def contacto(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '')
            correo = request.POST.get('correo2', '')
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
                name=name, correo=correo, phone=phone, ssr_apr=ssr_apr, 
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
                    
                    f"Datos Personales:\n"
                    f"• Nombre: {name}\n"
                    f"• Teléfono: {phone}\n"
                    f"• Comuna: {comuna}\n"
                    f"• Correo: {correo}\n\n"
                   
                    f"Detalles de SSR Y APR:\n"
                    f"• SSR/APR: {ssr_apr}\n"
                    f"• Cargo APR: {cargo_apr}\n"
                    f"• Cantidad Arranques: {cantidad}\n"
                    f"• Financiamiento: {radio}\n\n"
                    f"Mensaje: {message}\n\n"
                   
                    f"Página web Medidor Inteligente.")

            subject = 'Medidor Inteligente APR/SSR Contacto'
            email = "lisaisabelc19@gmail.com"
            cc_emails = [correo]
            send_email(subject, info, sender_email, password, email, cc_emails, smtp_server, smtp_port)

            
            return redirect('contacto')  # Redirigir a la página de contacto o donde corresponda

        except Exception as e:
            return render(request, 'app/e404.html', {'error': str(e)})  # Cambiar por una vista de error apropiad

    return render(request, 'app/contacto.html')
 
def send_email(subject, info, sender_email, password, email, cc_emails, smtp_server, smtp_port):
    server = None
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)

        msg = MIMEText(info, _charset='utf-8')
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = email
        msg['Cc'] = ', '.join(cc_emails)

        all_recipients = [email] + cc_emails
        server.sendmail(sender_email, all_recipients, msg.as_string())
        print('Email sent successfully!')

    except smtplib.SMTPException as e:
        print(f"Error: Email could not be sent. {e}")
        
    finally:
        if server:
            server.quit()

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

def error_404(request, exception):
    try:
        return render(request, 'app/e404.html', status=404)
    except Exception as e:
        logger.error(f"Error al renderizar la página 404: {e}", exc_info=True)
        return HttpResponseServerError("Página no encontrada, pero ocurrió un error al cargar la plantilla.")

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