from re import template
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product
from cart.forms import CartAddProductForm


class Index(ListView):
    model = Product
    template_name = "index.html"


def product_detail(request, pk, slug):
    product = get_object_or_404(Product, pk=pk, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(
        request,
        "product/detail.html",
        {"product": product, "cart_product_form": cart_product_form},
    )
