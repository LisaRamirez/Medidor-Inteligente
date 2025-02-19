from django.urls import path
from.views import home, clientes, contacto, nosotros, recursos, soluciones,apr

urlpatterns = [
    path('', home, name="home"),
    path('clientes/', clientes, name="clientes"),
    path('contacto/', contacto, name="contacto"),
    path('nosotros/', nosotros, name="nosotros"),
    path('recursos/', recursos, name="recursos"),
    path('soluciones/', soluciones, name="soluciones"),
    path('apr/', apr, name="apr"),
]
# Compare this snippet from medidor/app/models.py:
