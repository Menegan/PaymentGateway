from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'customer_name', 'customer_email', 'amount', 'status', 'reference', 'created_at', 'updated_at']
        read_only_fields = ['id', 'status', 'reference', 'created_at', 'updated_at']