# payment/serializers.py

from rest_framework import serializers
from .models import Payment
from cart.models import Cart


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'cart', 'is_successful', 'created_at']
        read_only_fields = ['id', 'created_at']
