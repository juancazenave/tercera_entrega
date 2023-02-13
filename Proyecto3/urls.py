from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('appproyecto3/', include('AppProyecto3.urls'))
]
