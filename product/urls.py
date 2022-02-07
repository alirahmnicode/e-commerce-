from django.urls import path
from .views import (Index,ProductDetailview)

app_name = "product"

urlpatterns = [
    path('' , Index.as_view() , name="index"),
    path('product/<int:pk>/<str:slug>/' , ProductDetailview.as_view() , name="detail"),
]
