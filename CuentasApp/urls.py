from django.contrib import admin
from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    # path('', views.home, name='home'),
    # path('error404/', views.Error, name='error404'),
    # path('lista_usuarios/', views.UsuarioLista.as_view(), name='listaUsuarios'),
    # path('detalle_usuario/<pk>', views.UsuarioDetalle.as_view(), name='detalleUsuario'),
    # path('crear_usuario/', views.UsuarioCrear.as_view(), name='crearUsuario'),
    # path('actualizar_usuario/<pk>', views.UsuarioActualizar.as_view(), name='actualizarUsuario'),
    # path('eliminar_usuario/<pk>', views.UsuarioEliminar.as_view(), name='eliminarUsuario'),

    path('', views.acceso, name='Acceso'),
    path('login/', views.loginVista, name='Login'),
    path('registro/', views.registroUsuario, name='Registro'),
    path('logout/', LogoutView.as_view(template_name="users/logout.html"), name='Logout'),
    path('editar-perfil/', views.editarUsuario, name='Edicion'),
    # path('ver_perfil/<int:usuario_id>/', views.verPerfilUsuario, name='ver_perfil_usuario'),
    # path('ver_perfil/<int:pk>/', views.PerfilDetalle.as_view(), name='detallePerfil'),


]