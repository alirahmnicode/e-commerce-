from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from api.filters import ProductFilter
from .pagination import DefaultPagination
from .serializers import ProductSerializer
from product.models import Product

# if query params in url filter object by category
# else return all objects
class ProductsApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name", "description", "category__name"]
    ordering_fields = ["price", "update", "discount_peresen", "sales_count"]
    filterset_class = ProductFilter


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
