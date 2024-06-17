from django.db import models


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen1 = models.ImageField(upload_to='productos', null=False, blank=False)
    imagen2 = models.ImageField(upload_to='productos', null=False, blank=False)
    imagen3 = models.ImageField(upload_to='productos', null=False, blank=True)
    imagen4 = models.ImageField(upload_to='productos', null=False, blank=True)

    def __str__(self):
        return self.nombre
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    producto = models.ManyToManyField(Producto)
    def __str__(self):
        return self.nombre
    
