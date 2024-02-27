from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'user', 'is_successful', 'created_at')
    list_filter = ('is_successful', 'created_at')
    search_fields = ('user__username', 'user__email', 'cart__id')
    readonly_fields = ('id', 'cart', 'user', 'created_at')


admin.site.register(Payment, PaymentAdmin)
