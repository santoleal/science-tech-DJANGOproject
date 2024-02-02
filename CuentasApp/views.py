from django.shortcuts import render
from . import models 

# Create your views here.


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView


class UsuarioLista(ListView):
    model = models.Usuario
    template_name = "lista_usuarios.html"
    context_object_name = "usuarios"


class UsuarioDetalle(DetailView):
    model = models.Usuario
    template_name = "detalle_usuarios.html"
    context_object_name = "usuario" 


class UsuarioCrear(CreateView):
    model = models.Usuario
    template_name = "crear_usuario.html"
    fields = ["nombre", "apellido"]
    success_url = '/BlogApp/'

class UsuarioActualizar(UpdateView):
    model = models.Usuario
    template_name = "actualizar_usuario.html"
    fields = ["__all__"]
    success_url = '/BlogApp/lista_usuarios'
    context_object_name = "usuario" 

   

class UsuarioEliminar(DeleteView):
    model = models.Usuario
    template_name = "eliminar_usuario.html"
    success_url = '/BlogApp/'