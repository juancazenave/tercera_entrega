from django.shortcuts import render, redirect
from django.http import HttpResponse

from AppProyecto3.models import *

# Create your views here.
# def curso(request):
#     curso = Curso(nombre='Python',camada='2345')
#     curso.save()
#     respuesta = f'Curso: {curso.nombre}, Camada: {curso.camada}'
#     return HttpResponse(respuesta)

def padre(request):
    return render(request, "AppProyecto3/padre.html")

def inicio(request):
    return render(request, "AppProyecto3/inicio.html")

def cursos(request):
    
    if request.method == 'POST':
        nuevo_curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
        nuevo_curso.save()
        return render(request, "AppProyecto3/inicio.html")

    return render(request, "AppProyecto3/cursos.html")

def entregables(request):
    return render(request, "AppProyecto3/entregables.html")

def estudiantes(request):

    if request.method == 'POST':
        nuevo_est = Estudiante(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'])
        nuevo_est.save()
        return render(request, "AppProyecto3/inicio.html")

    return render(request, "AppProyecto3/estudiantes.html")

def profesores(request):

    if request.method == 'POST':
        nuevo_est = Profesor(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'], profesion=request.POST['profesion'])
        nuevo_est.save()
        return render(request, "AppProyecto3/inicio.html")
    
    return render(request, "AppProyecto3/profesores.html")

def curso_formulario(request):

    if request.method == 'POST':
        nuevo_curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
        nuevo_curso.save()
        return render(request, "AppProyecto3/inicio.html")

    return render(request, "AppProyecto3/curso-formulario.html")

def buscar_camada(request):
    return render(request, "AppProyecto3/buscar-camada.html")

def buscar(request):
    
    if request.GET['camada']:
        mi_camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=mi_camada)

        return render(request, 'AppProyecto3/resultados-busqueda.html', {'cursos': cursos, 'camada': mi_camada})

    else:
        respuesta = 'No se encontro esa camada'
    
    return HttpResponse(respuesta)

    return HttpResponse(respuesta)