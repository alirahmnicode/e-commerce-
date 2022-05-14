from django.urls import path
from . import views


urlpatterns = [
    path("products/", views.ProductsApiView.as_view()),
    path("products/detail/<int:pk>/", views.ProductDetailView.as_view()),
]
