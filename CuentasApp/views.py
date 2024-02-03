from . import models 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,UserChangeForm
from django.shortcuts import render
from .forms import FormularioEdicionUsuario




# Create your views here.

# Se opta por utilizar un CRUD de clase para asociar campos de modelos a formularios
# class UsuarioLista(ListView):
#     model = models.Usuario
#     template_name = "lista_usuarios.html"
#     context_object_name = "usuarios"

# class UsuarioDetalle(DetailView):
#     model = models.Usuario
#     template_name = "detalle_usuarios.html"
#     context_object_name = "usuario" 

# class UsuarioCrear(CreateView):
#     model = models.Usuario
#     template_name = "crear_usuario.html"
#     fields = ["nombre", "apellido"]
#     success_url = 'lista_usuarios'

# class UsuarioActualizar(UpdateView):
#     model = models.Usuario
#     template_name = "actualizar_usuario.html"
#     fields = ["__all__"]
#     success_url = 'lista_usuarios'
#     context_object_name = "usuario" 

# class UsuarioEliminar(DeleteView):
#     model = models.Usuario
#     template_name = "eliminar_usuario.html"
#     success_url = 'lista_usuarios'
#     context_object_name = "usuario" 



def loginVista(request):
    if request.method == "POST":
        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            pwd = data["password"]

            user = authenticate(username = usuario, password = pwd)

            if user:
                login(request, user)
                return render(request, "users/aviso.html", {"Login": True, "mensaje": f"Bienvenido, {usuario}"})
            
            
        return render(request, "users/aviso.html", {"mensaje": f"No pudiste ingresar, datos incorrectos"})
     
    else:
        miFormulario = AuthenticationForm()
    return render(request, "users/login.html", {"miFormulario": miFormulario})



def registroUsuario(request):
    if request.method == "POST":
        miFormulario = UserCreationForm(request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            miFormulario.save()
      
            return render(request, "users/aviso.html", {"Registro": True, "mensaje": f"Usuario {usuario} creado con éxito."})
        else:
            return render(request, "users/aviso.html", {"mensaje": f"No pudiste concretar, datos incorrectos"})
          
    else:
        miFormulario = UserCreationForm()
    return render(request, "users/registro.html", {"miFormulario": miFormulario})
    


def acceso(request):
    return render(request, "users/vista_acceso.html")





def editarUsuario(request):

    usuario = request.user

    if request.method == 'POST':
        miFormulario = FormularioEdicionUsuario(request.POST, instance=request.user)
        
        if miFormulario.is_valid():
        
            data = miFormulario.cleaned_data
            usuario.firs_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.email = data['email']
            usuario.set_password(data['password1'])

            usuario.save()
      
            return render(request, "users/aviso.html", {"Edicion": True, "mensaje": f"Usuario {usuario} editado con éxito."})
        else:
            return render(request, "users/editar_usuario.html", {"miFormulario": miFormulario})
          
    else:
        miFormulario = FormularioEdicionUsuario(instance=usuario)
        return render(request, "users/editar_usuario.html", {"miFormulario": miFormulario, "usuario": usuario})



# def verPerfilUsuario(request, usuario_id):
#     usuario = models.User.objects.get(id = usuario_id)  
#     return render(request, "users/ver_perfil.html", {"usuario": usuario})


# class PerfilDetalle(DetailView):
#     model = models.User
#     template_name = "users/ver_perfil.html"
#     context_object_name = "usuario" 