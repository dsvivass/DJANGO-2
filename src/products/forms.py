# Este archivo no aparece por defecto, yo lo cree

from django import forms 

from .models import Product

# Primera forma más fácil de crear formularios
class ProductForm(forms.ModelForm):

    # Debo poner el mismo nombre de la variable y el campo para que se 
        # hagan cambios
    title = forms.CharField(label='',
                        widget=forms.TextInput(
                            attrs={
                                'placeholder': 'Inserte titulo',
                            })
                        )

    description = forms.CharField(required=False, 
                                widget=forms.Textarea(
                                    attrs={
                                        'class': 'newClassName two',
                                        'id': 'test',
                                        'rows': 20,
                                        'cols': 60
                                    }
                                ))

    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    # Voy a poner una condición para la validación del title
    # la sintaxis es la siguiente para el nombre del método:  
    #            def clean_<my_field_name>

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')

        if not len(title) > 5:
            raise forms.ValidationError("El título debe ser mayor a 5 caracteres")

        if not "Daniel" in title:
            raise forms.ValidationError("El título no contiene 'Daniel'")

        return title


# Segunda forma para crear formularios
class RawProductForm(forms.Form):
    # Los puedo dejar default o ponerles atributos y cambiar los widgets

    title = forms.CharField(label='',
                            widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'Inserte titulo',

                                })
                            )

    description = forms.CharField(required=False, 
                                widget=forms.Textarea(
                                    attrs={
                                        'class': 'newClassName two',
                                        'id': 'test',
                                        'rows': 20,
                                        'cols': 60
                                    }
                                ))
    price = forms.DecimalField(initial=199.99)