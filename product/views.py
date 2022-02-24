from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView
from django.http import JsonResponse

from .models import Product, CategoryForProduct
from .similar_product import similar
from .product_list import ProductList


class Index(ListView):
    model = Product
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_product"] = get_list_or_404(Product)[:10]
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


def product_list(request , query):
    if request.method == 'GET':
        next_products = request.GET.get('n')
        category = request.GET.get('category')
        product_list = ProductList(query , category)
        if not next_products:
            products = product_list.get_product()
            return render(request , "product/products_list.html",{"products": products})
        else:
            products = product_list.get_product(next_products)
            # create dict for response
            return JsonResponse(products,safe=False)
