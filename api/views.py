from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .listing_objects import Listing
from product.models import Product

# if query params in url filter object by category
# else return all objects
class ProductsApiView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get("category")
        if category is not None:
            queryset = queryset.filter(category__name=category)
        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# listing n object in each request
class ListingProductView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        next_products = request.GET.get("n")
        if next_products:
            listing = Listing(queryset=queryset)
            products = listing.listing_obj(range=next_products)
            serializer = ProductSerializer(products, many=True)
            return Response(data=serializer.data)
