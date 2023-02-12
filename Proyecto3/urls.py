from django.contrib import admin
from django.urls import path
from .views import saludo, segunda_vista, diadehoy, mi_nombre_es, probando_template
from AppProyecto3.views import curso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', saludo),
    path('segundavista/', segunda_vista),
    path('dia-de-hoy/', diadehoy),
    path('mi-nombre-es/<nombre>', mi_nombre_es),
    path('probando-template/', probando_template),
    path('curso/', curso)
]
