from django.urls import path
from .views import (Index,product_detail)

app_name = "product"

urlpatterns = [
    path('' , Index.as_view() , name="index"),
    path('product/<int:pk>/<str:slug>/' , product_detail , name="detail"),
]
