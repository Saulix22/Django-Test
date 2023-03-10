from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Material(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Imagen')
    area = models.CharField(max_length=30, null=True, verbose_name='Area')
    cantidad = models.IntegerField(default=0, verbose_name='Cantidad')

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Área: " + self.area
        return fila 
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        
class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=40, verbose_name='Titulo')
    fecha = models.DateField(auto_now_add=True, verbose_name='Fecha de creación')
    detalles = models.TextField(max_length=100, verbose_name='Detalles')
    cantidad = models.IntegerField(default=0, verbose_name='Cantidad solicitada')
    
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    id_material = models.ForeignKey(Material, on_delete=models.PROTECT)
    
    def __str__(self):
        fila = "Solicitud: " + self.titulo + " - " + "Cantidad: " + str(self.cantidad)
        return fila
    
    def delete(self, using=None, keep_parents=False):
        super().delete()