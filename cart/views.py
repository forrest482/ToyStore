from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from store.models import Product


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Try to get the latest unpaid cart for the user
    cart = Cart.objects.filter(user=request.user, is_paid=False).last()

    if not cart:
        # If there's no unpaid cart, create a new one
        cart = Cart.objects.create(user=request.user)

    # Now proceed to add the item to the cart
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product)

    if not created:
        # If the item is already in the cart, just increase the quantity
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')  # Redirect to the cart detail view


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(
        user=request.user, is_paid=False)
    return render(request, 'cart/cart_detail.html', {'cart': cart})
