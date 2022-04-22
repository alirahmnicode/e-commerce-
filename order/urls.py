from django.urls import path
from .views import PaymentView, OrderProductsView

app_name = "order"

urlpatterns = [
    path("payment/", PaymentView.as_view(), name="payment"),
    path("order-product/", OrderProductsView.as_view(), name="order_product"),
]
