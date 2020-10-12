from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaInicio, name='paginaInicio'),
    path('contacto.html', views.contacto, name='contacto'),
    path('index.html', views.paginaInicio, name='paginaInicio'),
    path('rescatados.html', views.mostrarRescatados , name='rescatados'),



]