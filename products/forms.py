from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre') 
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio')
    description = forms.CharField(max_length=200, label='Descripcion')
    available = forms.BooleanField(initial=True ,label='Disponible')
    image = forms.ImageField( label='Imagen del producto', required=False) 

    def save(self):
        name = forms.CharField(max_length=100, label='Nombre')
        description = forms.CharField(max_length=200, label='Description')
        price = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio')
        available = forms.BooleanField(initial=True ,label='Disponible', required = False)
        image = forms.ImageField(label="Photo", required=False)

        def save(self):
            Product.objects.create(
                name = self.cleaned_data['name'],
                description = self.cleaned_data['description'],
                price = self.cleaned_data['price'],
                available = self.cleaned_data['available'],
                image = self.cleaned_data['image']
            )
            