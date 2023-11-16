from django.db import models
from django.contrib.auth.models import User

#-------------TABLAS DE PILOTOS-------------------

class Piloto_Matias(models.Model):    
    puntos = models.CharField('Puntaje actual', max_length=60)
    carreras_ganadas = models.CharField('Carreras Ganadas', max_length=60 )
    fechas_completadas = models.CharField('Fechas Completadas', max_length=60)
    
    def __str__(self):
        return self.puntos
    
class Piloto_Fernando(models.Model):    
    puntos = models.CharField('Puntaje actual', max_length=60)
    carreras_ganadas = models.CharField('Carreras Ganadas', max_length=60 )
    fechas_completadas = models.CharField('Fechas Completadas', max_length=60)
    
    def __str__(self):
        return self.puntos    

class Piloto_Jordy(models.Model):    
    puntos = models.CharField('Puntaje actual', max_length=60)
    carreras_ganadas = models.CharField('Carreras Ganadas', max_length=60 )
    fechas_completadas = models.CharField('Fechas Completadas', max_length=60)
    
    def __str__(self):
        return self.puntos

class Piloto_Pato(models.Model):    
    puntos = models.CharField('Puntaje actual', max_length=60)
    carreras_ganadas = models.CharField('Carreras Ganadas', max_length=60 )
    fechas_completadas = models.CharField('Fechas Completadas', max_length=60)
    
    def __str__(self):
        return self.puntos

class Piloto_Cristian(models.Model):    
    puntos = models.CharField('Puntaje actual', max_length=60)
    carreras_ganadas = models.CharField('Carreras Ganadas', max_length=60 )
    fechas_completadas = models.CharField('Fechas Completadas', max_length=60)
    
    def __str__(self):
        return self.puntos
    
class Piloto_Martincho(models.Model):    
    puntos = models.CharField('Puntaje actual', max_length=60)
    carreras_ganadas = models.CharField('Carreras Ganadas', max_length=60 )
    fechas_completadas = models.CharField('Fechas Completadas', max_length=60)
    
    def __str__(self):
        return self.puntos
    
class Piloto_Yoa(models.Model):    
    puntos = models.CharField('Puntaje actual', max_length=60)
    carreras_ganadas = models.CharField('Carreras Ganadas', max_length=60 )
    fechas_completadas = models.CharField('Fechas Completadas', max_length=60)
    
    def __str__(self):
        return self.puntos

class Piloto_Guada(models.Model):    
    puntos = models.CharField('Puntaje actual', max_length=60)
    carreras_ganadas = models.CharField('Carreras Ganadas', max_length=60 )
    fechas_completadas = models.CharField('Fechas Completadas', max_length=60)
    
    def __str__(self):
        return self.puntos
    
class Piloto_Julian(models.Model):    
    puntos = models.CharField('Puntaje actual', max_length=60)
    carreras_ganadas = models.CharField('Carreras Ganadas', max_length=60 )
    fechas_completadas = models.CharField('Fechas Completadas', max_length=60)
    
    def __str__(self):
        return self.puntos

class Piloto_Nicolas(models.Model):    
    puntos = models.CharField('Puntaje actual', max_length=60)
    carreras_ganadas = models.CharField('Carreras Ganadas', max_length=60 )
    fechas_completadas = models.CharField('Fechas Completadas', max_length=60)
    
    def __str__(self):
        return self.puntos
        
class Piloto_Alejandro(models.Model):    
    puntos = models.CharField('Puntaje actual', max_length=60)
    carreras_ganadas = models.CharField('Carreras Ganadas', max_length=60 )
    fechas_completadas = models.CharField('Fechas Completadas', max_length=60)
    
    def __str__(self):
        return self.puntos                                 

#----------------TABLA DE FECHAS-----------------------


class Fechas_Carreras(models.Model):
    nombre = models.CharField('Carrera', max_length=100)
    fecha = models.DateField('Fecha', max_length=60)
    hora = models.TimeField('Hora', max_length=60)
    lugar = models.CharField('Pista', max_length=100)
    estado = models.CharField('Ganador', max_length=100, blank=True)
    
    def __str__(self):
        return self.nombre