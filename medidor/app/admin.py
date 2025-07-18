from django.contrib import admin
from .models import Contacto, Apr, Testimonio
# Register your models here.


class ContactoAdmin(admin.ModelAdmin):
    nombre = "name"
    correo = "correo"
    telefono = "phone"
    cargo = "cargo_apr"
    list_display = ('id',nombre, correo, telefono, 'ssr_apr',cargo , 'comuna', 'fecha', 'radio')
    search_fields = (nombre, 'comuna')
    list_filter = [nombre]
    ordering = (nombre, correo, telefono, 'ssr_apr',cargo , 'comuna', 'fecha', 'radio')
    list_per_page = 15

class AprAdmin(admin.ModelAdmin):
    nombre = "nameapr"
    list_display = ('id',nombre, 'comuna', 'region')
    search_fields = (nombre, 'comuna', 'region')
    list_filter = (nombre, 'comuna', 'region')
    ordering = (nombre, 'comuna', 'region')
    list_per_page = 15

class TestimonioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion', 'activo')
    search_fields = ('titulo', 'fecha_creacion', 'activo')
    list_filter = ('titulo', 'fecha_creacion', 'activo')
    ordering = ('titulo', 'fecha_creacion', 'activo')
    list_per_page = 15

admin.site.register(Testimonio, TestimonioAdmin)
admin.site.register(Apr, AprAdmin)
admin.site.register(Contacto, ContactoAdmin)