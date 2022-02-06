from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Product

# Create your views here.
class Index(ListView):
    model = Product
    template_name = 'index.html'
    