from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('error404/', views.Error, name='error404'),
    path('lista_usuarios/', views.UsuarioLista.as_view(), name='listaUsuarios'),
    path('detalle_usuario/<pk>', views.UsuarioDetalle.as_view(), name='detalleUsuario'),
    path('crear_usuario/', views.UsuarioCrear.as_view(), name='crearUsuario'),
    path('actualizar_usuario/<pk>', views.UsuarioActualizar.as_view(), name='actualizarUsuario'),
    path('eliminar_usuario/<pk>', views.UsuarioEliminar.as_view(), name='eliminarUsuario'),


]