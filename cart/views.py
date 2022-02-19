from itertools import product
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from .cart import Cart
from product.models import Product


class CartView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        return render(request, "cart/cart.html", {"cart": cart})


def add_to_cart(request, product_id, act):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    # if ajax request
    if is_ajax(request) and request.method == "POST":
        if act == "plus" or act == "add":
            quantity = 1
        else:
            quantity = -1
        context = cart.add(product, quantity=quantity)
        return JsonResponse(context, safe=False)
    # if wsgi request
    elif request.method == "POST":
        cart.add(product)
        return redirect(request.META.get("HTTP_REFERER"))


def remove(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        cart = Cart(request)
        cart.remove(product_id)
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        return redirect(request.META.get("HTTP_REFERER"))


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    print("ali" * 20)
    return redirect(request.META.get("HTTP_REFERER"))


# check ajax request
def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"
