from django.db import models
from django.utils import timezone
from django.shortcuts import render

# Create your models here.
class Documento(models.Model):
    titulo = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.titulo




class Contacto(models.Model):
    name = models.CharField("Nombre",max_length=100,null=True)
    correo = models.EmailField("Correo Electrónico",null=True)
    phone = models.CharField("Numero de Telefono",max_length=12,null=True, blank=True)
    ssr_apr = models.CharField("ssr o apr",max_length=100,null=True, blank=True)
    cargo_apr = models.CharField("Cargo en comité Apr",max_length=100,null=True, blank=True)
    comuna = models.CharField("Comuna",max_length=100,null=True, blank=True)
    cantidad = models.IntegerField("Cantidad de Apr",null=True, blank=True)
    fecha = models.DateTimeField("Fecha",default=timezone.now,null=True, blank=True)
    radio = models.CharField("Tipo de financiamiento",max_length=20, null=True, blank=True)
    message = models.TextField("Mensaje:",null=True, blank=True)

    def __str__(self):
        return self.name


opciones_consultas = [
    ["Arica y Parinacota", "Arica y Parinacota"],
    ["Tarapacá", "Tarapacá"],
    ["Antofagasta", "Antofagasta"],
    ["Atacama", "Atacama"],
    ["Coquimbo", "Coquimbo"],
    ["Valparaíso", "Valparaíso"],
    ["Metropolitana de Santiago", "Metropolitana de Santiago"],
    ["O'Higgins", "O'Higgins"],
    ["Maule", "Maule"],
    ["Ñuble", "Ñuble"],
    ["Biobío", "Biobío"],
    ["La Araucanía", "La Araucanía"],
    ["Los Ríos", "Los Ríos"],
    ["Los Lagos", "Los Lagos"],
    ["Aysén", "Aysén"],
    ["Magallanes", "Magallanes"],
]

class Apr(models.Model):
    nameapr = models.CharField("Nombre APR",max_length=100,null=True)
    comuna = models.CharField("Comuna",max_length=100,null=True, blank=True)
    region = models.CharField("Región",choices = opciones_consultas,max_length=100,null=True, blank=True)
    presidente = models.CharField("Presidente",max_length=100,null=True, blank=True)
    secretario= models.CharField("Secretario",max_length=100,null=True, blank=True)
    tesorero = models.CharField("Tesorero",max_length=100,null=True, blank=True)
    facebook = models.CharField("Facebook",max_length=100,null=True, blank=True)
    twitter = models.CharField("Twitter",max_length=100,null=True, blank=True)
    instagram = models.CharField("Instagram",max_length=100,null=True, blank=True)
    direccion = models.CharField("Dirección",max_length=100,null=True, blank=True)
    phone = models.CharField("Teléfono",max_length=24,null=True, blank=True)
    correo = models.EmailField("Correo Electrónico",null=True, blank=True)
    socios = models.IntegerField("Número de Socios",null=True, blank=True)
    horario = models.CharField("Horario de Atención",max_length=100,null=True, blank=True)
    mapa = models.CharField("Mapa",max_length=100,null=True, blank=True)
    activo = models.BooleanField("Activo",default=True)
    imagen = models.ImageField("Imagen",upload_to='apr',null=True, blank=True)

    
    
    def __str__(self):
        return self.nameapr

class Testimonio(models.Model):
    titulo = models.CharField("Título",max_length=100,null=True)
    sub_titulo = models.CharField("Subtítulo",max_length=100,null=True)
    fecha = models.DateTimeField("Fecha",null=True, blank=True)
    creador = models.CharField("Creador",max_length=100,null=True, blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now,null=True)
    contenido = models.TextField("Contenido",null=True)
    id_yt = models.CharField("Link Youtube",max_length=100,null=True, blank=True)
    check_yt = models.BooleanField(default=False,null=True)
    likes = models.PositiveIntegerField(default=0)
    activo = models.BooleanField("Activo",default=True)
    descripcion = models.CharField("Palabras Clave",max_length=100,null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        
        ordering = ['-fecha']  # más recientes primero

class ImagenTestimonio(models.Model):
    imagen = models.ImageField("Imagen", upload_to='testimonios', null=True)
    testimonio = models.ForeignKey(Testimonio, related_name='imagenes', on_delete=models.CASCADE)

