from django.db import models

# Create your models here.


class Reservacion(models.Model):
    puestos= models.IntegerField( verbose_name=u'Numero de puestos')
    puestos_con_gerentes= models.IntegerField( verbose_name=u'Numero de puestos con gerentes')

        
    class Meta:
        verbose_name = "Puesto"
        verbose_name_plural = "Puestos"


class Area(models.Model):
    nombre= models.CharField(max_length=200, verbose_name=u'Área')
    
    def __str__(self):
        return self.nombre
        
    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"
        
        
class Usuarios(models.Model):
    correo= models.CharField(max_length=200, verbose_name=u'Correo corporativo')
    nombre= models.CharField(max_length=200, verbose_name=u'Nombres')
    fecha_reserva= models.DateField(verbose_name=u'Fecha de reserva')
    area= models.ForeignKey(Area,on_delete=models.CASCADE,verbose_name=u'Área',default="")

    def __str__(self):
        return self.nombre
        
    class Meta:
        verbose_name = "Reservacion"
        verbose_name_plural = "Reservaciones"


