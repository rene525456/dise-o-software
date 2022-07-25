from django.db import models

# Create your models here.
class Cliente(models.Model):
    listaGenero=(
        ('femenino', 'Femenino'),
        ('masculino', 'Masculino'),
    )
    
    cliente_id = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length=10, null = False, unique = True)
    nombres = models.CharField(max_length=70, null = False)
    apellidos = models.CharField(max_length=70, null = False)
    genero = models.CharField(max_length=15, choices = listaGenero, null = False, default="femenino")
    
    correo = models.EmailField(max_length=100, null = False)
    telefono = models.CharField(max_length=15, null = False)
    celular = models.CharField(max_length=15, null = False)
    direccion = models.TextField(max_length=75, null = False, default = "Dirección")
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.cedula