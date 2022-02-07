from re import template
from django.shortcuts import render
from django.views.generic import ListView , DetailView

from .models import Product


class Index(ListView):
    model = Product
    template_name = 'index.html'



class ProductDetailview(DetailView):
    model = Product
    template_name = 'product/detail.html'

