from django.contrib import admin
from django.urls import path

#imports de las vistas de la aplicación
from . import views

urlpatterns = [
    path('searchComics/', views.pruebaListView.as_view()),
]