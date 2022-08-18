from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class cliente(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    vehiculo = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f' {self.nombre} {self.apellido} - {self.vehiculo}'

    

class mecanico(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)


    def __str__(self) -> str:
        return f' {self.nombre} {self.apellido}'


class reparacion(models.Model):
    Desperfecto = models.CharField(max_length=80)
    fechaDeEntrega = models.DateField()
    
   
    def __str__(self) -> str:
        return f' {self.Desperfecto} - {self.fechaDeEntrega}'

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null= True)