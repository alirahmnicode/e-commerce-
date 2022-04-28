from django.urls import path
from .views import PaymentView, OrderProductsView , OrdersView , VerifyOrderView , order_list

app_name = "order"

urlpatterns = [
    path("payment/", PaymentView.as_view(), name="payment"),
    path("order-product/", OrderProductsView.as_view(), name="order_product"),
    path("order-list/", OrdersView.as_view(), name="order_list"),
    path("order-verify/", VerifyOrderView.as_view(), name="order_verify"),
    path("test/", order_list, name="test"),
]
