from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    suttitulo = models.CharField(max_length=200)
    fecha = models.DateField()
    autor = models.ForeignKey(
        "auth.User",
        on_delete = models.CASCADE,
    )
    cuerpo = models.TextField()
    etiquetas = models.ManyToManyField('Etiqueta')
    categorias = models.ManyToManyField('Categoria')
    #imagen = 

    def __str__(self):
        return self.titulo
    
    # Esto es para referenciar a la URL absoluta del post
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    # Esto es para mostrar mejor la info en el dashbord y donde se haga referencia
    class Meta():
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ('fecha',)



class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse("categoria_detail", kwargs={"pk": self.pk})
    
    class Meta():
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("etiqueta_detail", kwargs={"pk": self.pk})
    
    class Meta():
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"
    


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comentarioss')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=300)
    fecha = models.DateField()

    def __str__(self):
        return f"Comentado por {self.autor} en {self.post}"
    
    def get_absolute_url(self):
        return reverse("comentarios_detail", kwargs={"pk": self.pk})
    
    class Meta():
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
