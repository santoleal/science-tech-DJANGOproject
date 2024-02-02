from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, AbstractUser


# Create your models here.


class Usuario(AbstractUser):
    edad = models.PositiveIntegerField(null=True, blank=True)
    rol = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username
    
    

