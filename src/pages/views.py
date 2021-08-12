from django.shortcuts import render
from django.shortcuts import HttpResponse 

# Create your views here.

# Aquí es donde vamos a crear varias cosas para nuestra página,
# Views es el lugar donde podré manejar varias de nuestras paginas,
# Y lo haremos usando funciones o clases

def homeView(request, *args, **kwargs): # Cada función llega con un request definido
    print(request.user)                 # Este request.user es fundamental, así vemos quién solicita esto
    # return HttpResponse("<h1>Hello World!</h1>") # Esto sirve, pero ahora vamos a manejar templates

    return render(request, "home.html", {})

def contactView(request, *args, **kwargs):
    return render(request, "contact.html", {})

def aboutView(request, *args, **kwargs):
    myContext = {
        'text': 'This is about us',
        'numero': 123,
        'list': [123, 456, 789, 'abc'],
        'titulo': '<h1>Titulo</h1>'
    }
    return render(request, "about.html", myContext)