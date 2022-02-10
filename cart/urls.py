from django.urls import path
from .views import CartView, AddToCartView , clear_cart

app_name = "cart"

urlpatterns = [
    path("", CartView.as_view(), name="index"),
    path("add/<int:product_id>/", AddToCartView.as_view(), name="add"),
    path("clear/", clear_cart, name="clear"),
]
