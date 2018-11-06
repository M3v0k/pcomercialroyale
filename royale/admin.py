from django.contrib import admin
from royale.models import Tipo, Level, Carta

#Registramos nuestras clases principales.
admin.site.register(Tipo)
admin.site.register(Level)
admin.site.register(Carta)

# Register your models here.
