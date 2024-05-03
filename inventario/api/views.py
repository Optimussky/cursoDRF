from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from inventario.models import Producto
from inventario.api.serializer import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Producto.objects.all()  # queryset es el conjunto de datos con los que va a trabajar Django
    serializer_class = ProductoSerializer # aquí en serializer_class se le pasa lo que va a serializar, en este caso ProductoSerializer
