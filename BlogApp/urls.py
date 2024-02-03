from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('error404/', views.Error, name='error404'),
    # path('categoria/', views.categoria, name='categoria'),
    # path('etiqueta/', views.etiqueta, name='etiqueta'),
    # path('comentarios/', views.comentario, name='comentarios'),
    path('categorias/', views.listaCategorias, name='categorias'),
    path('categorias/<str:nombre>', views.listaPostCategoria, name='lista_categoria'),
    path('post/<int:pk>/', views.PostDetalle.as_view(), name='detallePost'),
    path('post/archivo/', views.PostsLista.as_view(), name='listaPosts'),
    path('post/crear_post/', views.PostCrear.as_view(), name='crearPost'),
    path('post/actualizar_post/<int:pk>/', views.PostActualizar.as_view(), name='actualizarPost'),
    path('post/eliminar_post/<int:pk>/', views.PostEliminar.as_view(), name='eliminarPost'),
    # path('post/ultimos_posts/', views.UltimosPost.as_view(), name='ultimos_posts'),

    

]