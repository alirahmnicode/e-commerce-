from product.models import Product
from django.shortcuts import get_object_or_404
from decimal import Decimal


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            # save an empty cart in the session
            cart = self.session["cart"] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"] = product
        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item["quantity"] for item in self.cart.values())

    def add(self, product, quantity=1):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        # add
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0, "price": str(product.price)}
        # update
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

        price = self.cart[product_id]["quantity"] * int(self.cart[product_id]["price"])
        quantity = self.cart[product_id]["quantity"]
        return {
            "quantity": quantity,
            "price": price,
        }


    def remove(self, product_id):
        """
        Remove a product from the cart.
        """
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def clear(self):
        # remove cart from session
        del self.session["cart"]
        self.save()

    def save(self):
        self.session.modified = True
