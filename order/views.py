from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from .models import Order
from .trackingcode import tracking_code

from cart.cart import Cart
from users.models import Profile
from product.models import Product


class PaymentView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, "order/paymant.html", {"cart": cart})


class OrderProductsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                cart = Cart(request)
                # create order instance
                order = Order()
                # set values
                order.price_paid = cart.get_total_price()
                order.user_info = profile
                order.trackingcode = tracking_code()
                order.payment = True
                order.save()
                # set products
                for product_id in cart.cart:
                    product = Product.objects.get(pk=product_id)
                    order.products.add(product.pk)
                cart.clear()
                messages.success(request, "Your purchase has been successfully registered , you can see factors in dashboard")
                return redirect(request.META.get("HTTP_REFERER"))
            except:
                messages.error(request, "Your purchase has been not registered.if you have not profile , create in dashboard")
                return redirect(request.META.get("HTTP_REFERER"))
        else:
            messages.error(request, "Your are not logged in")
            return redirect(request.META.get("HTTP_REFERER"))
