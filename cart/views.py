from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .cart import Cart
from .forms import CartAddProductForm
from product.models import Product


class CartView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        print(cart)
        return render(request, "cart/cart.html", {"cart": cart})


class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        # create Cart instance
        cart = Cart(request)
        product = get_object_or_404(Product, id=kwargs["product_id"])
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product, quantity=cd["quantity"], override_quantity=cd["override"])
        return redirect(request.META.get("HTTP_REFERER"))


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    print("ali" * 20)
    return redirect(request.META.get("HTTP_REFERER"))
