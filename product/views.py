from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView

from .models import Product, CategoryForProduct
from .similar_product import similar


class Index(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_categories"] = get_list_or_404(CategoryForProduct)[:10]
        context["recommends"] = Product.objects.filter(recommend=True)[:10]
        context["bestsellers"] = Product.objects.all().order_by("-sales_count")[:10]
        return context


def product_detail(request, pk, slug):
    product = get_object_or_404(Product, pk=pk, slug=slug)
    similar_posts = similar(pk)
    return render(
        request,
        "product/detail.html",
        {"product": product, "similar_posts": similar_posts},
    )


def get_products_by_category(request, category):
    products = get_list_or_404(Product, category__name=category)
    return render(
        request,
        "product/products_list.html",
        {"products": products, "category": category},
    )
