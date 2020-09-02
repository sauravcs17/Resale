from urllib import request

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from .models import Product,ProductImages


class ProductForm(forms.ModelForm):
        #owner = forms.CharField(label='owner',widget=forms.TextInput(attrs={'placeholder':'Enter Your Username','class':'form-control','id':'search-bar','required':''}))
        class Meta:
            model = Product
            fields = ['name','description', 'condition', 'image', 'price', 'brand','category','Phone','location','email']
            exclude=['owner','slug','email','Phone']


        # fields = ['name', 'description','condition','image','price','created','brand','slug','Phone']
        # exclude = [' owner']
class ImageForm(forms.ModelForm):
        class Meta:
             model=ProductImages
             fields=['FILE',]
             exclude=['product',]
