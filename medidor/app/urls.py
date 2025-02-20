from django.urls import path
from.views import home, clientes, contacto, nosotros, recursos, soluciones,apr,e404

urlpatterns = [
    path('', home, name="home"),
    path('clientes/', clientes, name="clientes"),
    path('contacto/', contacto, name="contacto"),
    path('nosotros/', nosotros, name="nosotros"),
    path('recursos/', recursos, name="recursos"),
    path('soluciones/', soluciones, name="soluciones"),
    path('apr/<int:apr_id>/', apr, name="apr"),
    path('e404/', e404, name="e404"),
]
# Compare this snippet from medidor/app/models.py:
