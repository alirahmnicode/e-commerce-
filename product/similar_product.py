from django.shortcuts import get_object_or_404 , get_list_or_404
from django.db.models import Count
from .models import Product


def similar(pk):
    product = get_object_or_404(Product , pk=pk)
    product_categoreis_ids = product.category.values_list('id' , flat=True)
    similar_product = Product.objects.filter(category__in=product_categoreis_ids).exclude(id=product.id)
    similar_product = similar_product.annotate(same_category=Count('category'))
    print(similar_product)
    return similar_product
