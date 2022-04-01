from django.urls import path
from .views import index, product_detail, get_products_by_category , product_list , search

app_name = "product"

urlpatterns = [
    path("", index, name="index"),
    path("product/<int:pk>/<str:slug>/", product_detail, name="detail"),
    path("product/<str:category>/", get_products_by_category, name="pr_ct_list"),
    path("products/list/<str:category>/", product_list, name="product_list"),
    path("products/search/", search, name="search"),
]
