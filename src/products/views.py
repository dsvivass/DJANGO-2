from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
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



# (VISUALIZACIÓN) De listas de datos
def productListView(request):

    # Casi siempre se llama querySet
    querySet = Product.objects.all() # List of objects

    context = {
        'objectList': querySet
    }

    return render(request, "product/products.html", context)




# (ESCRITURA)
def productCreateView(request):

    # Puedo poner datos iniciales
    initialData = {
        'title': 'My Daniel title',
    }

    form = ProductForm(request.POST or None, initial=initialData) # Crea la instancia de la clase
                        # Ya sea con información o vacío

    if form.is_valid():
        form.save()
        form = ProductForm() # Lo re-renderizo para que salga blank y ahí sé que algo pasó

    context = {
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


# (MODIFICACION)
def productModifyView(request):

    # Puedo poner datos iniciales de un objeto por defecto
    obj = Product.objects.get(id=1)

    form = ProductForm(request.POST or None, instance=obj) # Crea la instancia de la clase
                        # Ya sea con información o vacío

    if form.is_valid():
        form.save()
        form = ProductForm() # Lo re-renderizo para que salga blank y ahí sé que algo pasó

    context = {
        'form': form
    }

    return render(request, 'product/modify.html', context)




# Dynamic URL Routing
def dynamicLookupView(request, my_id):

    # obj = Product.objects.get(id=my_id) # Lo podría hacer así, pero voy a usar una herramienta
                                    # que me ayuda a lidiar con datos no encontrados

    # Forma de manejar objetos no encontrados
    obj = get_object_or_404(Product, id=my_id)

    # Otra forma de lidiar con errores, pero la de arriba es más sencilla
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404

    context = {
        "object": obj
    }

    return render(request, 'product/detail.html', context)



# (ELIMINACION)
def productDelete(request, id):

    obj = get_object_or_404(Product, id=id)

    # POST request, NUNCA eliminar con un GET request
    if request.method == "POST":
        obj.delete()
        return redirect("../../")


    context = {
        "object": obj
    }

    return render(request, 'product/delete.html', context)