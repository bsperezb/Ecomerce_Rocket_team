from rest_framework import serializers
from ecommerce.models.ecommerce import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['ref_code', 'user', 'items', 'start_date', 'ordered_date', 'ordered']