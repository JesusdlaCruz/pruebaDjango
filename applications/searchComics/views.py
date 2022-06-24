from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Import del servicio que hace la petición GET a la API
from .services import apiReq
# Vistas genéricas para la applicacion

class pruebaListView(ListView):    
    #Muestra en el template prueba.html de la peticion GET a la API      
    template_name = 'prueba.html'
    datos = apiReq()
    context_object_name = 'marvelAPIResults'
    queryset = datos
