from django.urls import path
from .views import ProductsApiView, ProductDetailView , ListingProductView


urlpatterns = [
    path("products/", ProductsApiView.as_view()),
    path("products/detail/<int:pk>/", ProductDetailView.as_view()),
    path("products/list/", ListingProductView.as_view()),
]
