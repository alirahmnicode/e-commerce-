from django.urls import path
from .views import CartView, AddToCartView

app_name = "cart"

urlpatterns = [
    path("", CartView.as_view(), name="index"),
    path("add/<int:pk>/", AddToCartView.as_view(), name="add"),
]
