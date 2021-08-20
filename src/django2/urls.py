"""django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import homeView, contactView, aboutView
from products.views import productDetailView, productCreateView, productCreateViewClasico, productCreateViewClasicoPureDjango

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('home/', homeView, name='home'),
    path('contact/', contactView, name='contact'),
    path('about/', aboutView, name='about'),
    path('product/', productDetailView, name='product'),
    path('create/', productCreateView, name='create'),
    path('createClasico/', productCreateViewClasico, name='createClasico'),
    path('createPureDjango/', productCreateViewClasicoPureDjango, name='createPureDjango'),
]
