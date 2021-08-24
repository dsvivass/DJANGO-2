from django.db import models
from django.urls import reverse

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

    # Dynamic linking of URL
    def getAbsoluteUrl(self):
        # return reverse("dynamicLookupView", kwargs={'my_id': self.id}) # Aquí pongo el name de la url al que quiera redirigir, con los parámetros correspondientes
        return reverse("productos:dynamicLookupView", kwargs={'my_id': self.id}) # Le debo pasar aquí productos: ya que como cambie el
                                    # path de las urls.py a products/urls.py y ahi defini el 
                                    # 
                                    #              app_name = 'productos'     
                                    # 
                                    # y es de donde quiero sacar el dynamicLookupView, para no confundirlo
                                    # con alguna url que tenga también el nombre name='dynamicLookupView'