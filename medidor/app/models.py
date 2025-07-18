from django.db import models
from django.utils import timezone
from django.shortcuts import render

# Create your models here.
class Documento(models.Model):
    titulo = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.titulo

class testimonio(models.Model):
    titulo = models.CharField("Título",max_length=100,null=True)
    sub_titulo = models.CharField("Subtítulo",max_length=100,null=True)
    fecha = models.DateTimeField("Fecha",null=True)
    creador = models.CharField("Creador",max_length=100,null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now,null=True)
    contenido = models.TextField("Contenido",null=True)
    id_yt = models.CharField("Link Youtube",max_length=100,null=True)
    check_yt = models.BooleanField(default=False,null=True)
    activo = models.BooleanField("Activo",default=True)

    def __str__(self):
        return self.titulo

class ImagenTestimonio(models.Model):
    testimonio = models.ForeignKey(testimonio, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField("Imagen", upload_to='testimonios', null=True)



class Contacto(models.Model):
    name = models.CharField("Nombre",max_length=100,null=True)
    correo = models.EmailField("Correo Electrónico",null=True)
    phone = models.CharField("Numero de Telefono",max_length=12,null=True)
    ssr_apr = models.CharField("ssr o apr",max_length=100,null=True)
    cargo_apr = models.CharField("Cargo en comité Apr",max_length=100,null=True)
    comuna = models.CharField("Comuna",max_length=100,null=True)
    cantidad = models.IntegerField("Cantidad de Apr",null=True)
    fecha = models.DateTimeField("Fecha",default=timezone.now,null=True)
    radio = models.CharField("Tipo de financiamiento",max_length=20, null=True)
    message = models.TextField("Mensaje:",null=True)

    def __str__(self):
        return self.name


opciones_consultas = [
    
    ["Coquimbo","Coquimbo"],
    ["Valparaíso","Valparaíso"],
    ["Metropolitana","Metropolitana"],
    ["O'higgins","O'higgins"],
    ["Maule","Maule"],
    ["Biobio","Biobio"],
    ["Araucania","Araucania"],
    ["Los Rios","Los Rios"],
    ["Los Lagos","Los Lagos"],
    ["Aysen","Aysen"],
    
]

class Apr(models.Model):
    nameapr = models.CharField("Nombre APR",max_length=100,null=True)
    comuna = models.CharField("Comuna",max_length=100,null=True)
    region = models.CharField("Región",choices = opciones_consultas,max_length=100,null=True)
    presidente = models.CharField("Presidente",max_length=100,null=True)
    secretario= models.CharField("Secretario",max_length=100,null=True)
    tesorero = models.CharField("Tesorero",max_length=100,null=True)
    facebook = models.CharField("Facebook",max_length=100,null=True)
    twitter = models.CharField("Twitter",max_length=100,null=True)
    instagram = models.CharField("Instagram",max_length=100,null=True)
    direccion = models.CharField("Dirección",max_length=100,null=True)
    phone = models.CharField("Teléfono",max_length=24,null=True)
    correo = models.EmailField("Correo Electrónico",null=True)
    socios = models.IntegerField("Número de Socios",null=True)
    horario = models.CharField("Horario de Atención",max_length=100,null=True)
    mapa = models.CharField("Mapa",max_length=100,null=True)
    activo = models.BooleanField("Activo",default=True)
    imagen = models.ImageField("Imagen",upload_to='apr',null=True)

    
    
    def __str__(self):
        return self.nameapr