from django.shortcuts import redirect, render
from django.views import View
from .cart import Cart


class CartView(View):
    def get(self,request,*args, **kwargs):
        context = {
            'cart':request.session['cart']
        }
        return render(request , 'cart/cart.html',context)


class AddToCartView(View):
    def get(self,request,*args, **kwargs):
        # create Cart instance
        cart = Cart(request)
        cart.get_product(kwargs['pk'])
        # save in session
        cart.save()
        return redirect(request.META.get('HTTP_REFERER'))
