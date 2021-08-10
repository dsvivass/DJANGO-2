from django.contrib import admin

# Register your models here.
from .models import Product # Importo el modelo Product recien creado,
                        # Para verlo en el panel de administracion

admin.site.register(Product)


