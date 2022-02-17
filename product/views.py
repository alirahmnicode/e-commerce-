from re import template
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product


class Index(ListView):
    model = Product
    template_name = "index.html"


def product_detail(request, pk, slug):
    product = get_object_or_404(Product, pk=pk, slug=slug)
    return render(
        request,
        "product/detail.html",
        {"product": product},
    )
