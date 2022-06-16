from django.db import models
from django import forms

from .models import Product

# Create your models here.

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price'
        ]