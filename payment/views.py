from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import get_messages
from cart.models import Cart
from .models import Payment


def list_payments(request):
    payments = Payment.objects.filter(
        user=request.user).order_by('-created_at')
    return render(request, 'payment/list_payments.html', {'payments': payments})


def payment_result(request, cart_id, is_successful):
    cart = get_object_or_404(
        Cart, id=cart_id, user=request.user, is_paid=False)
    is_successful = is_successful == 'True'

    # Clear existing messages
    storage = get_messages(request)
    for message in storage:
        # This loop will clear all messages
        pass

    if request.method == "POST":
        Payment.objects.create(cart=cart, user=request.user,
                               is_successful=is_successful)
        if is_successful:
            cart.is_paid = True
            cart.save()
            messages.success(
                request, "Your payment was successful. Thank you for your purchase!")
        else:
            messages.error(
                request, "Your payment was unsuccessful. Please try again.")

        return render(request, 'payment/payment_result.html', {'is_successful': is_successful})
    return redirect('cart_detail', cart_id=cart.id)
