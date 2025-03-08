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
            return redirect('e404')  # Redirige a la página de error
        
        # Obtener todos los objetos de Apr
        appr = Apr.objects.all()
        data = {'apr': appr}
        
        return render(request, 'app/clientes.html', data)

    except Exception as e:
        print(f"Unexpected error: {e}")
        messages.error(request, 'Hubo un problema con tu solicitud.')
        return redirect('e404')  # Redirige a la página de error




def filtrar_apr(request):
    try:
        # Verificar si hay parámetros GET inesperados
        if not request.GET.get('region'):
            messages.error(request, 'Parámetros no permitidos o faltantes en la solicitud.')
            return redirect('e404')  # Redirige a la página de error

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
        return redirect('e404')  # Redirige a la página de error

    






def apr(request, apr_id):
    try:
        apppr = get_object_or_404(Apr, id=apr_id)  # get_object_or_404 ya maneja errores
        data = {'appr': apppr}
        return render(request, 'app/apr.html', data)
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        messages.error(request, 'Hubo un problema al cargar la información.')
        return redirect('e404')  # Redirige a una página de error




def home(request):
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            phone = request.POST.get('phone', '').strip()
            ssr_apr = request.POST.get('ssr_apr', '').strip()
            cargo_apr = request.POST.get('cargo_apr', '').strip()
            comuna = request.POST.get('comuna', '').strip()
            cantidad = request.POST.get('cantidad', '').strip()
            radio = request.POST.get('financiamiento', '').strip()
            message = request.POST.get('message', '').strip()
            fecha = datetime.now()

            # Validación básica
            if not name or not email or not phone:
                messages.error(request, 'Nombre, correo y teléfono son obligatorios.')
                return redirect('home')

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

            cc_emails = ['contacto@medidorinteligente.cl']
            subject = 'APR/SSR Contacto'

            send_email(subject, info, sender_email, password, email, cc_emails, smtp_server, smtp_port)

            messages.success(request, 'Tu mensaje ha sido enviado correctamente')
            return redirect('home')  # Redirige a la vista principal después de enviar

        except ValidationError as ve:
            logger.error(f"Error de validación: {ve}")
            messages.error(request, 'Datos inválidos. Verifica e intenta nuevamente.')
            return redirect('home')

        except IntegrityError as ie:
            logger.error(f"Error de integridad en la base de datos: {ie}")
            messages.error(request, 'Error al guardar en la base de datos.')
            return redirect('home')

        except Exception as e:
            logger.error(f"Error inesperado: {e}", exc_info=True)
            messages.error(request, 'Hubo un error al procesar tu solicitud. Inténtalo nuevamente.')
            return redirect('e404')  # Redirige a una página de error personalizada

    return render(request, 'app/home.html')



def contacto(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            phone = request.POST.get('phone', '').strip()
            ssr_apr = request.POST.get('ssr_apr', '').strip()
            cargo_apr = request.POST.get('cargo_apr', '').strip()
            comuna = request.POST.get('comuna', '').strip()
            cantidad = request.POST.get('cantidad', '').strip()
            radio = request.POST.get('financiamiento', '').strip()
            message = request.POST.get('message', '').strip()
            fecha = datetime.now()

            # Guardar en la base de datos
            contacto = Contacto(
                name=name, email=email, phone=phone, ssr_apr=ssr_apr, 
                cargo_apr=cargo_apr, comuna=comuna, cantidad=cantidad, 
                fecha=fecha, radio=radio, message=message
            )
            contacto.save()

            # Configuración de correo
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
                f"• Fecha: {fecha.strftime('%d-%m-%Y %H:%M:%S')}\n\n"
                f"Información de Financiamiento:\n"
                f"• Financiamiento: {radio}\n\n"
                f"Mensaje: {message}\n\n"
                f"Quedamos a tu disposición para cualquier consulta adicional.\n\n"
                f"Atentamente,\n"
                f"El equipo de atención al cliente de Medidor Inteligente."
            )

            cc_emails = ['contacto@medidorinteligente.cl']
            subject = 'APR/SSR Contacto'

            send_email(subject, info, sender_email, password, email, cc_emails, smtp_server, smtp_port)

            messages.success(request, 'Tu mensaje ha sido enviado correctamente')
            return redirect('contacto')

        except Exception as e:
            logger.error(f"Error en la vista contacto: {e}", exc_info=True)
            messages.error(request, 'Hubo un error al procesar tu solicitud. Inténtalo nuevamente.')
            return redirect('contacto')  # Redirige a la misma página de contacto
        
        except SMTPException as e:
            logger.error(f"Error al enviar el correo: {e}", exc_info=True)
            messages.error(request, 'Hubo un problema al enviar el correo. Inténtalo nuevamente.')

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
        logger.error(f"Error al renderizar la página 'nosotros': {e}", exc_info=True)
        return HttpResponseServerError("Hubo un error al cargar la página. Inténtalo más tarde.")




def soluciones(request):
    try:
        return render(request, 'app/soluciones.html')
    except Exception as e:
        logger.error(f"Error al renderizar la página 'soluciones': {e}", exc_info=True)
        return HttpResponseServerError("Hubo un error al cargar la página. Inténtalo más tarde.")

def recursos(request):
    try:
        return render(request, 'app/recursos.html')
    except Exception as e:
        logger.error(f"Error al renderizar la página 'recursos': {e}", exc_info=True)
        return HttpResponseServerError("Hubo un error al cargar la página. Inténtalo más tarde.")

def error_404(request, exception=None):
    try:
        return render(request, 'app/e404.html', status=404)
    except Exception as e:
        logger.error(f"Error al renderizar la página 404: {e}", exc_info=True)
        return HttpResponseNotFound("Página no encontrada, pero ocurrió un error al cargar la plantilla.")

def prueba(request):
    try:
        return render(request, 'app/prueba.html')
    except Exception as e:
        logger.error(f"Error al renderizar la página 'prueba': {e}", exc_info=True)
        return HttpResponseServerError("Hubo un error al cargar la página. Inténtalo nuevamente más tarde.")




def test_logging():
    logger.info("Este es un mensaje informativo.")
    logger.warning("Advertencia: Algo podría estar mal.")
    logger.error("Error: Algo falló.")
    logger.critical("¡Error crítico!")