from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer
from cart.models import Cart
from django.shortcuts import get_object_or_404


class ListPaymentsAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # This method will automatically filter the payments by the current user
        return Payment.objects.filter(user=self.request.user).order_by('-created_at')


class ProcessPayment(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        cart_id = request.data.get('cart')
        is_successful = request.data.get('is_successful', 'false').lower() in [
            'true', '1', 't', 'y', 'yes']

        # Retrieve the user's active cart, ensuring it exists and belongs to the user
        cart = get_object_or_404(
            Cart, id=cart_id, user=request.user, is_paid=False)

        # Create a Payment instance
        payment = Payment.objects.create(
            cart=cart, user=request.user, is_successful=is_successful)

        # Update the cart's paid status if the payment is successful
        if is_successful:
            cart.is_paid = True
            cart.save()

        serializer = self.get_serializer(payment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
