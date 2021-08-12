from django.shortcuts import render
from .models import Product
# Create your views here.

def productDetailView(request):

    obj = Product.objects.get(id=1)
    # context = {   # Esto sirve pero tiene problemas para cuando hacemos cambios
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price
    # }

    context = { # Es mejor pasar todo el objeto
        'object': obj
    }

    return render(request, 'product/detail.html', context)
