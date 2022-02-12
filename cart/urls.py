from django.urls import path
from .views import CartView, AddToCartView , clear_cart , remove

app_name = "cart"

urlpatterns = [
    path("", CartView.as_view(), name="index"),
    path("add/<int:product_id>/", AddToCartView.as_view(), name="add"),
    path("remove/", remove, name="remove"),
    path("clear/", clear_cart, name="clear"),
]
