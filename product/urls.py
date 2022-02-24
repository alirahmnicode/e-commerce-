from django.urls import path
from .views import Index, product_detail, get_products_by_category , product_list

app_name = "product"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("product/<int:pk>/<str:slug>/", product_detail, name="detail"),
    path("product/<str:category>/", get_products_by_category, name="pr_ct_list"),
    path("products/list/<str:query>/", product_list, name="product_list"),
]
