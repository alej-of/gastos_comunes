from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Departamento(models.Model):
    numero = models.CharField(unique=True, blank=False)
    metros_2 = models.IntegerField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    extras = models.ManyToManyField('Extra', related_name='departamentos', blank=True)

    def __str__(self):
        return f"Departamento {self.numero} - {self.metros_2} m²"
    
class Extra(models.Model):
    nombre = models.CharField(max_length=45, blank=False, unique=True)
    porcentaje = models.FloatField(blank=False)

    def __str__(self):
        return self.nombre
    
    def clean(self):
        if not (0.0 <= self.porcentaje <= 1.0):
            raise ValidationError("El porcentaje debe estar entre 0% y 100%.")