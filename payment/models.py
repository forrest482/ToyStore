# payment/models.py
from django.db import models
from django.conf import settings
from cart.models import Cart


class Payment(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='payments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    is_successful = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Cart {self.cart.id} by {self.user.username}"
