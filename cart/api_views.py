# cart/api_views.py
from rest_framework import generics, permissions
from store.models import Product
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from django.shortcuts import get_object_or_404


class CartDetail(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Fetch the latest unpaid cart for the user or create a new one if none exist
        cart = Cart.objects.filter(
            user=self.request.user, is_paid=False).last()
        if not cart:
            cart = Cart.objects.create(user=self.request.user)
        return cart


class AddItemToCart(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Fetch the latest unpaid cart for the user or create a new one if none exist
        cart = Cart.objects.filter(
            user=self.request.user, is_paid=False).last()
        if not cart:
            cart = Cart.objects.create(user=self.request.user)

        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)

        # Check if the product is already in the cart
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product)

        if not created:
            # Update the quantity if the item already exists
            cart_item.quantity += serializer.validated_data.get('quantity', 1)
            cart_item.save()
        else:
            # If it's a new item, save it with the provided quantity
            serializer.save(cart=cart, product=product)


class UpdateCartItem(generics.UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(cart__user=self.request.user)
