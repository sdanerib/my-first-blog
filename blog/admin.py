from django.contrib import admin
from .models import Post #importamos modelo creado


# Register your models here.
#Para hacer nuestro modelo visible en la página del administrador, tenemos que registrar el
#modelo
admin.site.register(Post)
