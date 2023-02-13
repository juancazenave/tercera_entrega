from django.urls import path

from AppProyecto3.views import inicio, profesores, estudiantes, cursos, entregables

urlpatterns = [
    path('', inicio),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('cursos/', cursos),
    path('entregables/', entregables),
    
]
