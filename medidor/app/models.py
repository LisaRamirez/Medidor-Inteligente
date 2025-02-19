from django.db import models
from django.utils import timezone

# Create your models here.


class Contacto(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=12,null=True)
    ssr_apr = models.CharField(max_length=100,null=True)
    cargo_apr = models.CharField(max_length=100,null=True)
    comuna = models.CharField(max_length=100,null=True)
    cantidad = models.IntegerField(null=True)
    fecha = models.DateTimeField(default=timezone.now,null=True)
    radio = models.CharField(max_length=20, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name


class Apr(models.Model):
    nameapr = models.CharField(max_length=100,null=True)
    comuna = models.CharField(max_length=100,null=True)
    region = models.CharField(max_length=100,null=True)
    presidente = models.CharField(max_length=100,null=True)
    secretario= models.CharField(max_length=100,null=True)
    tesorero = models.CharField(max_length=100,null=True)
    facebook = models.CharField(max_length=100,null=True)
    twitter = models.CharField(max_length=100,null=True)
    instagram = models.CharField(max_length=100,null=True)
    direccion = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=12,null=True)
    email = models.EmailField(null=True)
    socios = models.IntegerField(null=True)
    horario = models.CharField(max_length=100,null=True)
    mapa = models.CharField(max_length=100,null=True)
    imagen = models.ImageField(upload_to='apr',null=True)

    
    
    def __str__(self):
        return self.name