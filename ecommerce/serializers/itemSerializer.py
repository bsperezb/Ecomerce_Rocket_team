from ecommerce.models.ecommerce import Item_Artesanias
from rest_framework import serializers

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item_Artesanias
        fields = ['name','price','description']
    
    def to_representation(self, instance):
        return{
            'id':instance.id,
            'name':instance.name,
            'price':instance.price,
            'description':instance.description,
            #'image':instance.image if instance.image != '' else ''        
        }