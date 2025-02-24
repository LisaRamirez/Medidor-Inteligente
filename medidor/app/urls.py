from django.urls import path
from.views import home, clientes, contacto, nosotros, recursos, soluciones,apr,e404, filtrar_apr
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
    path('e404/', e404, name="e404"),
    path('filtrar_apr/', filtrar_apr, name='filtrar_apr'),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Compare this snippet from medidor/app/models.py:
