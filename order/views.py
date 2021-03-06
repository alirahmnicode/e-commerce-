from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.views import View
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Order
from .trackingcode import tracking_code
from .ordering import Ordering
from .filters import OrderFilter

from cart.cart import Cart
from users.models import Profile
from product.models import Product
from product.inby import increase_buyer


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
                if len(cart) > 0:
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
                    increase_buyer(order)
                    messages.success(
                        request,
                        "Your purchase has been successfully registered , you can see factors in dashboard",
                    )
                    return redirect(request.META.get("HTTP_REFERER"))
                else:
                    messages.error(request, "Your purchase has been not registered.")
                    return redirect(request.META.get("HTTP_REFERER"))
            except:
                messages.error(
                    request,
                    "Your purchase has been not registered.if you have not profile , create in dashboard",
                )
                return redirect(request.META.get("HTTP_REFERER"))
        else:
            messages.error(request, "Your are not logged in")
            return redirect(request.META.get("HTTP_REFERER"))


class OrdersView(View):
    def get(self, request):
        # quereis
        order = request.GET.get("order")
        filter = request.GET.get("confirm")
        # objects
        orders = Order.objects.filter(payment=True)
        if order == 'true' and filter is None:
            o = Ordering(request.GET , queryset=orders)
            obj = o.order_obj()
        elif order != 'true' and filter:
            obj = OrderFilter(request.GET , queryset=orders).qs
        elif order == 'true' and filter:
            f = OrderFilter(request.GET , queryset=orders).qs
            o = Ordering(request.GET , queryset=f)
            obj = o.order_obj()
        else:
            obj = OrderFilter(request.GET , queryset=orders).qs
        form = OrderFilter(request.GET , queryset=orders).form
        paginator = Paginator(obj, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "order/orders.html", {"filter": page_obj , 'form':form})


class VerifyOrderView(View):
    def post(self, request):
        type_value = request.GET.get("type")
        obj_id = request.GET.get("id")
        order = get_object_or_404(Order, pk=obj_id)
        data = None
        if type_value == "status":
            if order.confirm:
                order.confirm = False
            else:
                order.confirm = True
        else:
            if order.post:
                order.post = False
            else:
                order.post = True
        order.save()
        data = {
            'status':order.confirm,
            'send':order.post
        }
        return JsonResponse(data)

