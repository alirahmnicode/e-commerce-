from django.shortcuts import render
from django.views import View

from cart.cart import Cart



class PaymentView(View):
    def get(self,request):
        cart = Cart(request)
        return render(request ,'order/paymant.html' , {'cart':cart})

