from django.shortcuts import render
from django.views import View



class PaymentView(View):
    def get(self,request):
        return render(request ,'order/paymant.html')

