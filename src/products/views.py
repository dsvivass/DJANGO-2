from django.shortcuts import render
from .models import Product
# Create your views here.

from .forms import ProductForm, RawProductForm

# (VISUALIZACION)
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




# (ESCRITURA)
def productCreateView(request):

    form = ProductForm(request.POST or None) # Crea la instancia de la clase

    if form.is_valid():
        form.save()
        form = ProductForm() # Lo re-renderizo para que salga blank y ahí sé que algo pasó

    context = { # Es mejor pasar todo el objeto
        'form': form
    }

    return render(request, 'product/create.html', context)





# (ESCRITURA)
# Así se hace de manera más rústica
def productCreateViewClasico(request):
    print(request.GET)
    print(request.POST)

    if request.method == "POST":
        newTitle = request.POST.get('my_titulo') # Este es un metodo muy malo para guardar datos, 
                                            # es muy pobre porque no estamos validando si son datos buenos o no
        print(newTitle)
        # Si lo quisiera guardar

        # Product.objects.create(title=newTitle) .....

    context = {}
    return render(request, 'product/createClasico.html', context)





# (ESCRITURA)
# Así se hace de manera pura en Django
def productCreateViewClasicoPureDjango(request):

    myForm = RawProductForm() # Aquí renderizo todo normal para ver el formulario  
                        # sin que nos bote errores por no llenar las casillas

    if request.method == "POST":
        myForm = RawProductForm(request.POST) # Creo la instancia de la clase

        if myForm.is_valid(): # Si ya se validó que todos los campos son válidos
            print(myForm.cleaned_data)
            Product.objects.create(**myForm.cleaned_data) # Puedo pasar los datos como kwargs

        else:
            print(myForm.errors)

    context = {
        'form': myForm
    }
    return render(request, 'product/createPureDjango.html', context)