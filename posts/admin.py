from django.contrib import admin
from .models import *

# Modelos para ser vistos y modificados desde el Django admin
admin.site.register(Departamento)
admin.site.register(Programa)
admin.site.register(Asignatura)
admin.site.register(Usuario)