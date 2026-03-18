from django.urls import path
from . import views  # Aquí importas todo el módulo views
from .views import (
    home, clientes, contacto, nosotros, recursos, soluciones, apr,
    filtrar_apr, prueba, testimonio, cargar_mas_testimonios, asistente_virtual, preguntas, tutoriales
)
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('', home, name="home"),
    path('clientes/', clientes, name="clientes"),
    path('contacto/', contacto, name="contacto"),
    path('nosotros/', nosotros, name="nosotros"),
    path('recursos/', recursos, name="recursos"),
    path('soluciones/', soluciones, name="soluciones"),
    path('apr/<int:apr_id>/', apr, name="apr"),
    path('testimonio/', testimonio, name="testimonio"),
    path('api/cargar-mas/', cargar_mas_testimonios, name='cargar_mas'),
    path('filtrar_apr/', filtrar_apr, name='filtrar_apr'),
    path('prueba/', prueba, name='prueba'),
    path('preguntas/', preguntas, name='preguntas'),
    path('tutoriales/', tutoriales, name='tutoriales'),
    



     path("asistente/", asistente_virtual, name="asistente_virtual"),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'app.views.error_404'

