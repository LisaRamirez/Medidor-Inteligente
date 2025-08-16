from django.urls import path
from.views import home, clientes, contacto, nosotros, recursos, soluciones,apr, filtrar_apr,prueba, testimonio, cargar_mas_testimonios, cargar_mas_testimonios
from django.conf import settings
from django.conf.urls.static import static

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
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'app.views.error_404'

# Compare this snippet from medidor/app/models.py:
