from django.urls import path
from .views import add_to_cart, cart_detail
from .api_views import CartDetail, AddItemToCart, UpdateCartItem

urlpatterns = [
    # Template-based views
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('detail/', cart_detail, name='cart_detail'),

    # API endpoints
    path('api/cart/', CartDetail.as_view(), name='api_cart_detail'),
    path('api/cart/add/<int:product_id>/',
         AddItemToCart.as_view(), name='api_add_item_to_cart'),
    path('api/cart/item/<int:pk>/update/',
         UpdateCartItem.as_view(), name='api_update_cart_item'),
]
