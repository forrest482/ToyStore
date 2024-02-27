from django.urls import path
from .views import payment_result, list_payments
from .api_views import ProcessPayment, ListPaymentsAPIView

urlpatterns = [
    # Template-based views
    path('payment-result/<int:cart_id>/<str:is_successful>/',
         payment_result, name='payment_result'),
    path('payments/', list_payments, name='list_payments'),


    # API endpoints
    path('api/process-payment/', ProcessPayment.as_view(), name='process_payment'),
    path('api/payments/', ListPaymentsAPIView.as_view(), name='api_list_payments')

]
