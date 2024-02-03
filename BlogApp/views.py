from . import models 
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from CuentasApp.models import Avatar

# Create your views here.


# página de inicio
def home(request):
    # es_principal = True 
    # posts = models.Post.objects.all().order_by('-fecha')[:2]
    # recent_posts = models.Post.published.order_by('-publish')[:2]
    # avatar = Avatar.objects.get(user=request.user.id)
    last_post_grande = models.Post.objects.filter(principal=True).order_by('-fecha')[:1] 
    last_post_chico = models.Post.objects.filter(secundarias=True).order_by('-fecha')[:2]
    contexto = {'last_post_grande':last_post_grande, 'last_post_chico':last_post_chico}
    return render(request, 'home/index.html',contexto )

# Error 404
def Error(request):
    return render(request, 'pages/error404.html', status=404)

# Se crean vistas de modelos creados

def post(request, id):
    posteo = get_object_or_404(models.Post, id=id)
    return render(request, 'pages/post.html',{"post_id": posteo} )


# Listado de items añadidos a base de datos
def listaPost(request):
    lista_posts = models.Post.objects.all()
    return render(request, 'pages/archivo.html', {"lista_post": lista_posts })

def listaCategorias(request):
    lista_categorias = models.Categoria.objects.all()
    return render(request, 'pages/categoria.html', {"lista_categorias": lista_categorias })


# Listado de posts por categorías añadidos a base de datos

def listaPostCategoria(request, nombre):
    categoria = get_object_or_404(models.Categoria, nombre=nombre)
    lista_posts_categoria = categoria.post_set.all()
    return render(request, 'pages/categoria.html', {"categoria": categoria,"lista_posts_categoria": lista_posts_categoria })



# Se crea vistas de formularios CRUD de los Post

# Se opta por utilizar un CRUD de clase para asociar campos de modelos a formularios
class PostsLista(ListView):
    model = models.Post
    template_name = "blog/lista_posts.html"
    context_object_name = "posts"

class PostDetalle(DetailView):
    model = models.Post
    template_name = "blog/post.html"
    context_object_name = "post" 

class PostCrear(CreateView):
    model = models.Post
    template_name = "blog/crear_post.html"
    fields = ['titulo', 'extracto', 'cuerpo', 'categoria', 'principal', 'secundarias']
    success_url = '/post/archivo/'

    # Función para validar al autor actual del post antes de guardarlo
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = models.Post
    template_name = "blog/actualizar_post.html"
    fields = ['titulo', 'extracto', 'cuerpo', 'categoria', 'principal', 'secundarias'] 
    success_url = '/post/archivo/'
    context_object_name = "post" 


class PostEliminar(LoginRequiredMixin, DeleteView):
    model = models.Post
    template_name = "blog/eliminar_post.html"
    success_url = '/post/archivo/'
    context_object_name = "post" 



# class UltimosPost(ListView):
#     model = models.Post
#     template_name = "blog/ultimos_posts.html"
#     context_object_name = "ultimos_posts"
#     ordering = ['-fecha']
#     paginate_by = 2

#     def get_queryset(self):
#         return models.Post.objects.all()[:6]