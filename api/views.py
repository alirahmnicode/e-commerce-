from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import ProductFilter
from .pagination import DefaultPagination
from .serializers import ProductSerializer, CartAddSerializer
from product.models import Product
from cart.cart import Cart


class ProductViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name", "description", "category__name"]
    ordering_fields = ["price", "update", "discount_peresen", "sales_count"]
    filterset_class = ProductFilter


class CartView(APIView):
    # return user cart
    def get(self, request):
        cart = Cart(request)
        data = {}
        for item in cart:
            serializer = ProductSerializer(instance=item["product"])
            data[serializer.data["pk"]] = serializer.data
            data[serializer.data["pk"]]["quantity"] = item["quantity"]
            data[serializer.data["pk"]]["total_price"] = item["total_price"]
        data["cart_total_price"] = cart.get_total_price()
        return Response(data=data, status=status.HTTP_200_OK)


class AddToCart(APIView):
    # add product to cart or update product quanity
    def post(self, request):
        # deserializing
        serializer = CartAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        product = get_object_or_404(Product, pk=int(data["product_id"]))
        quantity = data["quanity"]
        # add product to cart
        cart = Cart(request)
        cart.add(product=product, quantity=quantity)
        return Response(status=status.HTTP_201_CREATED)


class RemoveProductFromCart(APIView):
    # remove product from cart
    def post(self, request):
        product_id = request.data.get("product_id")
        if product_id:
            cart = Cart(request)
            cart.remove(product_id)
            return Response(
                data={"product removed from your cart"},
                status=status.HTTP_204_NO_CONTENT,
            )
        else:
            return Response(
                data={"product id not found"}, status=status.HTTP_400_BAD_REQUEST
            )


class ClearCart(APIView):
    def post(self, request):
        cart = Cart(request)
        cart.clear()
        return Response(status=status.HTTP_202_ACCEPTED)