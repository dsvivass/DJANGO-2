from django.db import models

# Create your models here.
# Quiero que mi back-end tenga memoria de mi producto

class Product(models.Model): # Usamos los modelfields de django, heredamos de models.Model
    
    # Yo quiero que estos atributos sean mapeados a la base de datos
    
    title = models.CharField(max_length=120) # max_length es obligatorio ponerlo
    description = models.TextField(blank=True, null=True) # blank en True indica que el campo 
                                                        # no debe ser llenado, y null True significa 
                                                        # que en la base de datos podrá tener un valor nulo
    price = models.DecimalField(max_digits=19, decimal_places=2)
    summary = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=True)