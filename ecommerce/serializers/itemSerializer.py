from ecommerce.models.ecommerce import Item_Artesanias
from rest_framework import serializers

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item_Artesanias
        fields = ['price', 'description']