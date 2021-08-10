from django.db import models

# Create your models here.
# Quiero que mi back-end tenga memoria de mi producto

class Product(models.Model): # Usamos los modelfields de django, heredamos de models.Model
    
    # Yo quiero que estos atributos sean mapeados a la base de datos
    
    title = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    summary = models.TextField(default='Valor por defecto')