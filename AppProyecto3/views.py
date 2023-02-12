from django.shortcuts import render
from django.http import HttpResponse

from AppProyecto3.models import Curso

# Create your views here.
def curso(request):
    curso = Curso(nombre='Python',camada='2345')
    curso.save()
    respuesta = f'Curso: {curso.nombre}, Camada: {curso.camada}'

    return HttpResponse(respuesta)