from django.db import models
from django.contrib import admin


class Tipo(models.Model):

    nombre  =   models.CharField(max_length=60, verbose_name="Nombre")
    detalle  =   models.CharField(max_length=60, verbose_name="Detalle",help_text="Describa el tipo")

    class Meta:
                verbose_name="Tipo"
                verbose_name_plural="Tipos"
                ordering = ["-nombre"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombre

class Level(models.Model):

    nombre  =   models.CharField(max_length=60)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    class Meta:
                verbose_name="Level"
                verbose_name_plural="Levels"
                ordering = ["-creado"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombre

    def __str__(self):

        return self.nombre


class Carta(models.Model):

    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(verbose_name="Imagen",upload_to="cartar",null=True,blank=True)
    detalle = models.CharField(max_length=200)
    nivel = models.ForeignKey(Level,on_delete=models.CASCADE,related_name="keynivel", help_text="Ingrese un numeros entero")
    tipos = models.ManyToManyField(Tipo,verbose_name="Tipo",related_name="keytipo")

    class Meta:
                verbose_name="Carta"
                verbose_name_plural="Cartas"
                ordering = ["-nivel"]

    def __str__(self):
        return self.nombre
