from django.urls import path , include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register("products", views.ProductViewSet)

urlpatterns = [
    path('' , include(router.urls)),
    path('cart/' , views.CartView.as_view()),
    path('cart/add/' , views.AddToCart.as_view()),
    path('cart/remove/' , views.RemoveProductFromCart.as_view()),
    path('cart/clear/' , views.ClearCart.as_view()),
]
