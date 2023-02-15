from django.urls import path

from AppProyecto3.views import inicio, profesores, estudiantes, cursos, entregables, padre, curso_formulario

urlpatterns = [
    path('', padre, name='padre'),
    path('inicio/', inicio, name='inicio'),
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('cursos/', cursos, name='cursos'),
    path('entregables/', entregables, name='entregables'),
    path('curso-formulario/', curso_formulario, name='curso-formulario')
    
]
