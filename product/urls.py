from django.urls import path
from .views import Index, product_detail, get_products_by_category

app_name = "product"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("product/<int:pk>/<str:slug>/", product_detail, name="detail"),
    path("product/<str:category>/", get_products_by_category, name="pr_ct_list"),
]
