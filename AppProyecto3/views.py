from django.shortcuts import render
from django.http import HttpResponse

from AppProyecto3.models import Curso

# Create your views here.
def curso(request):
    curso = Curso(nombre='Python',camada='2345')
    curso.save()
    respuesta = f'Curso: {curso.nombre}, Camada: {curso.camada}'
    return HttpResponse(respuesta)

def inicio(request):
    return render(request, "AppProyecto3/inicio.html")

def cursos(request):
    return render(request, "AppProyecto3/cursos.html")

def entregables(request):
    return render(request, "AppProyecto3/entregables.html")

def estudiantes(request):
    return render(request, "AppProyecto3/estudiantes.html")

def profesores(request):
    return render(request, "AppProyecto3/profesores.html")