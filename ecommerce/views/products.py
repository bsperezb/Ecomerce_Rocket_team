from rest_framework import status, viewsets
from rest_framework.response import Response

from ecommerce.serializers.itemSerializer import ItemSerializers

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializers

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()
        
    def list(self, request):
        itemSerializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(itemSerializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message:' 'This product was created correctly!!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            itemSerializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if itemSerializer.is_valid():
                itemSerializer.save()
                return Response(itemSerializer.data, status=status.HTTP_200_OK)
            return Response(itemSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        product = self.get_queryset().filter(id=pk).first() # get instance        
        if product:
            product.state = False
            product.save()
            return Response({'Message':'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'Error':'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
