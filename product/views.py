from django.shortcuts import render, get_object_or_404 , get_list_or_404
from django.views.generic import ListView, DetailView

from .models import Product , CategoryForProduct


class Index(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_categories'] = get_list_or_404(CategoryForProduct)[:10]
        return context


def product_detail(request, pk, slug):
    product = get_object_or_404(Product, pk=pk, slug=slug)
    return render(
        request,
        "product/detail.html",
        {"product": product},
    )
