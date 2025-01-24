from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_email', 'amount', 'status', 'reference', 'created_at')
    list_filter = ('status',)
    search_fields = ('customer_name', 'customer_email', 'reference')