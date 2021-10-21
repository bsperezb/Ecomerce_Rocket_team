from rest_framework import serializers
from ecommerce.models.ecommerce import OrderItem

class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['user','item','is_ordered','quantity',]