from django.db import models
from django.contrib.auth.models import User


class Ingeniero(models.Model):
    COD_ingeniero = models.AutoField(primary_key=True)
    Identificacion = models.IntegerField()
    Nombres = models.CharField(max_length=70)
    Apellidos = models.CharField(max_length=70)
    ROL = models.CharField(max_length=50) 
    Direccion = models.CharField(max_length=80)
    Telefono = models.IntegerField()
    Email = models.CharField(max_length=70) 
    #user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
# Create your models here.

type_id = [
    (1, 'Seleccione'),
    (2, 'Cedula de ciudadania'),
    (3, 'Cedula de extranjeria'),
    (4, 'NIT'),
    ]

class Cliente(models.Model):
    Tipo_de_identificacion = models.IntegerField(
        blank=False, null=False, 
        choices=type_id,
        default=1
    )
    NID = models.IntegerField(primary_key=True)
    Razon_social = models.CharField(max_length=70)
    Direccion = models.CharField(max_length=70)
    Email = models.CharField(max_length=70) 
    Telefono = models.IntegerField()
   
class Proyecto(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=500)
    Costo = models.FloatField(max_length=(9,2))
    #user = models.ForeignKey(User, null=True,  on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=True,  on_delete=models.CASCADE)
    ingenieros_a_cargo = models.ForeignKey(Ingeniero, null=True,  on_delete=models.CASCADE)
    ingenieros_a_cargo = models.ManyToManyField(Ingeniero)

   
class Actividad(models.Model):
    COD_actividad = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=500)
    Costo = models.FloatField(max_length=(9,2))
    user = models.ForeignKey(User, null=True,  on_delete=models.CASCADE)
    proyecto= models.ForeignKey(Proyecto, null=True,  on_delete=models.CASCADE)
    ingeniero= models.ForeignKey(Ingeniero, null=True,  on_delete=models.CASCADE)

'''numeroFuentes = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),   
    (5, 'Otro valor')
]'''

state = [
    (1, 'Seleccione'),
    (2, 'En proceso'),
    (3, 'Terminado')
]
type_font = [
    (1, 'Seleccione'),
    (2, 'RPG'),
    (3, 'RPGLE'),
    (4, 'RPGLE y RPG'),
    
]

workedFonts = [
    (1, 'Seleccione'),
    (2, 'RPG'),
    (3, 'RPGLE'),
]

class Bitacora(models.Model):
    Fecha = models.DateField()
    COD_bitacora = models.AutoField(primary_key=True)
    Nombre= models.CharField(max_length=40, null=True)
    Horas_laboradas = models.FloatField(max_length=5, null=False)
    cliente = models.ForeignKey(Cliente, null=True,  on_delete=models.CASCADE)
    Proyecto= models.ForeignKey(Proyecto, null=True,  on_delete=models.CASCADE)
    Actividad= models.ForeignKey(Actividad, null=True,  on_delete=models.CASCADE)
    Cantidad_de_fuentes_trabajados = models.IntegerField(null=False, blank=False)
    Tipos_de_fuentes_trabajados = models.IntegerField(
        null=False, blank=False,
        choices=type_font,
        default=1
    )
    Estado_de_los_fuentes_trabajados = models.IntegerField(
        null=False, blank=False,
        choices=state,
        default=1
    )
    
    Nota = models.TextField(max_length=300, null=True, blank=True,) 
    
    
    
   
