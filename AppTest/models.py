from django.db import models

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