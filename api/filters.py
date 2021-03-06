from dataclasses import fields
from django_filters.rest_framework import FilterSet
from product.models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            "category":["exact"],
            "options":["exact"],
            "available":["exact"],
            "recommend":["exact"],
            "price":['gt','lt']
        }
