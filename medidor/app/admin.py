from django.contrib import admin
from .models import Contacto, Apr
# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    nombre = "name"
    correo = "email"
    telefono = "phone"
    cargo = "cargo_apr"
    list_display = ('id',nombre, correo, telefono, 'ssr_apr',cargo , 'comuna', 'fecha', 'radio')
    search_fields = (nombre, 'comuna')
    list_filter = [nombre]
    ordering = (nombre, correo, telefono, 'ssr_apr',cargo , 'comuna', 'fecha', 'radio')
    list_per_page = 10

class AprAdmin(admin.ModelAdmin):
    nombre = "nameapr"
    list_display = ('id',nombre, 'comuna', 'region')
    search_fields = (nombre, 'comuna', 'region')
    list_filter = (nombre, 'comuna', 'region')
    ordering = (nombre, 'comuna', 'region')
    list_per_page = 10

admin.site.register(Apr, AprAdmin)
admin.site.register(Contacto, ContactoAdmin)
