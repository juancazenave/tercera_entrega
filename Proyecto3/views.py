from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola Ruti")

def segunda_vista(request):
    return HttpResponse("Segunda Vista")

def diadehoy(request):
    fechahoy = datetime.now()
    texto = f'Hoy es {fechahoy.strftime("%d/%m/%Y")}'
    return HttpResponse(texto)

def mi_nombre_es(request, nombre):
    texto = f'Mi nombre es {nombre}'
    return HttpResponse(texto)

def probando_template(request):
    #mi_html = open('C:/Users/User/Desktop/tercera entrega/Proyecto3/templates/template1.html')
    #Creo las variables que le voy a pasar al Template
    nombre = 'Juan'
    apellido = 'Cazenave'
    fechadehoy = datetime.now()
    lista_de_notas = [1, 3, 4, 9, 2]
    #Creo un diccionario para agrupar las variables que le paso al Template
    diccionario = {'nombre': nombre, 'apellido': apellido, 'fecha': fechadehoy, 'notas': lista_de_notas}
    #plantilla = Template(mi_html.read())
    #mi_html.close()
    plantilla = loader.get_template('template1.html')
    #contexto = Context(diccionario)
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

