# activos/models.py

from django.db import models

class Activo(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50, choices=[
        ('Datos', 'Datos'),
        ('Servicios', 'Servicios'),
        ('Software', 'Software'),
        ('Personal', 'Personal'),
    ])
    confidencialidad = models.IntegerField()
    integridad = models.IntegerField()
    disponibilidad = models.IntegerField()
    
    def __str__(self):
        return str(self.nombre)
