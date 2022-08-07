from rest_framework import serializers
from dashboard.models import Payment_Intent


class PaymentIntentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Intent
        fields = [
            'id',
            'amount',
            'order_id',
            'return_url',
            'user',
            'status'
        ]
