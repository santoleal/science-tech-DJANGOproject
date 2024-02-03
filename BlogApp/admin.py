from django.contrib import admin
from .models import Post, Categoria
# from datetime import datetime
from django.utils import timezone




# Esta clase es para visualizar de mejor forma la info en el dashboard del admin
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'categoria', 'fecha', 'antiguedad']
    search_fields = ['titulo', 'autor']
    list_filter = ['autor']

    def antiguedad(self, object):
        '''
        Se crea esta función para añadir un "campo virtual" o "campo calculado" en la vista de Post del admin, con la cantidad de días de antiguedad de la publicación.
        '''
        print('*********', object)
        if object.fecha:
            fecha_actual = timezone.now().date()
            fecha_post = timezone.localtime(object.fecha).date()
            return f'{(fecha_actual - fecha_post).days} días'



# Register your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Categoria)
# admin.site.register(Etiqueta)
# admin.site.register(Comentario)

