from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

    def __str__(self):
        return self.nombre + '(' + str(self.camada) + ')'

class Estudiante(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre + '(' + str(self.apellido) + ')' + '(' + str(self.email) + ')'


class Profesor(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + '(' + str(self.apellido) + ')' + '(' + str(self.email) + ')' + '(' + str(self.profesion) + ')'

class Entregable(models.Model):

    nombre = models.CharField(max_length=50)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return self.nombre + '(' + str(self.fecha_de_entrega) + ')' + '(' + str(self.entregado) + ')'

    