from product.models import Product
from django.shortcuts import get_object_or_404


class Cart:
    def __init__(self, request):
        self.request = request
        self.cart = request.session.get("cart")
        if not self.cart:
            self.cart = request.session["cart"] = {}
        self.product = None

    def get_product(self, pk):
        product = get_object_or_404(Product, pk=pk)
        self.product = product
        return product


    def save(self):
        product = self.product

        self.cart[product.pk] = {
            "quantity": 1,
            "name": product.name,
            "img": product.image.url,
        }
        self.request.session.modified = True