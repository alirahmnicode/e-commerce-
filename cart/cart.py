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
        # check that product removed or not
        self.removed_product = False

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
        if product_id not in self.cart and quantity != -1:
            print('updata'*20)
            self.cart[product_id] = {"quantity": quantity, "price": str(product.price)}
        # update
        elif product_id in self.cart:
            self.cart[product_id]["quantity"] += quantity
            # remove product that its quantity equal 0
            if self.cart[product_id]["quantity"] == 0:
                self.removed_product = self.remove(int(product_id))
        self.save()
        if not self.removed_product and  product_id in self.cart:
            price = self.cart[product_id]["quantity"] * int(self.cart[product_id]["price"])
            total_price = self.get_total_price()
            quantity = self.cart[product_id]["quantity"]
            return {
                "quantity": quantity,
                "price": price,
                'total_price':total_price,
                'remove':False
            }
        else:
            total_price = self.get_total_price()
            return {
                'remove':True,
                'total_price':total_price,
            }



    def remove(self, product_id):
        """
        Remove a product from the cart.
        """
        if str(product_id) in self.cart:
            del self.cart[str(product_id)]
        self.save()
        return True

    def clear(self):
        # remove the cart from session
        del self.session["cart"]
        self.save()

    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def save(self):
        self.session.modified = True
