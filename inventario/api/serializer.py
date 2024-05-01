from rest_framework import serializers
from inventario.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto# Esto es lo que va a serializar o deserializar
        fields = '__all__'
