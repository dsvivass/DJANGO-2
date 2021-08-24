from django.contrib import admin
from django.urls import path
from pages.views import homeView, contactView, aboutView
from products.views import productDetailView, productCreateView, productCreateViewClasico, productCreateViewClasicoPureDjango, productModifyView, dynamicLookupView, productDelete, productListView

app_name = 'productos' # Es el nombre especial que voy a usar para referirme a esta app,

urlpatterns = [

    path('product/', productDetailView, name='product'),
    path('create/', productCreateView, name='create'),
    path('createClasico/', productCreateViewClasico, name='createClasico'),
    path('createPureDjango/', productCreateViewClasicoPureDjango, name='createPureDjango'),
    path('modify/', productModifyView, name='modify'),
    path('<int:my_id>', dynamicLookupView, name='dynamicLookupView'), # Leer los tipos de args que puedo pasar
    path('<int:id>/delete', productDelete, name='delete'),
    path('', productListView, name='listView'),

]