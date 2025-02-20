from django.contrib import admin
from .models import Contacto, Apr
# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'phone', 'ssr_apr', 'cargo_apr', 'comuna', 'fecha', 'radio')
    search_fields = ('name', 'comuna')
    list_filter = ['name']
    ordering = ('name', 'email', 'phone', 'ssr_apr', 'cargo_apr', 'comuna', 'fecha', 'radio')
    list_per_page = 10

class AprAdmin(admin.ModelAdmin):
    list_display = ('id','nameapr', 'comuna', 'region')
    search_fields = ('nameapr', 'comuna', 'region')
    list_filter = ('nameapr', 'comuna', 'region')
    ordering = ('nameapr', 'comuna', 'region')
    list_per_page = 10

admin.site.register(Apr, AprAdmin)
admin.site.register(Contacto, ContactoAdmin)
