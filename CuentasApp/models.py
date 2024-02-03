from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.


# class Usuario(AbstractUser):
#     edad = models.PositiveIntegerField(null=True, blank=True)
#     rol = models.CharField(max_length=50, null=True, blank=True)
#     avatar = models.CharField(max_length=50, null=True, blank=True)

#     def __str__(self):
#         return self.username
    

#     class Meta():
#         verbose_name = 'Usuario'
#         verbose_name_plural = 'Usuarios'

#     groups.related_name = 'usuario_groups'
#     user_permissions.related_name = 'usuario_user_permissions'



class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", blank=True, null=True)

    