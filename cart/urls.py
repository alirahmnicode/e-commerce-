from django.urls import path
from .views import CartView,add_to_cart, clear_cart , remove

app_name = "cart"

urlpatterns = [
    path("", CartView.as_view(), name="index"),
    path("add/<int:product_id>/<str:act>/", add_to_cart, name="add"),
    path("remove/", remove, name="remove"),
    path("clear/", clear_cart, name="clear"),
]
