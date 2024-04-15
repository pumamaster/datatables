from rest_framework import serializers
from .models import *

class BaseSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        base_url = "https://res.cloudinary.com/dknltb45r/"

        for i in range(1, 6):
            foto_key = f"foto_{i}"
            if foto_key in data and data[foto_key]:
                data[foto_key] = f"{base_url}{data[foto_key]}"

        return data

class ArticuloSerializer(BaseSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class ArticuloUnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class EventoSerializer(BaseSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class PartidoSerializer(BaseSerializer):
    class Meta:
        model = Partido
        fields = '__all__'

class FotoDiaSerializer(BaseSerializer):
    class Meta:
        model = Foto_Día
        fields = '__all__'

class LogoSerializer(BaseSerializer):
    class Meta:
        model = Logo
        fields = '__all__'

class CartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carta
        fields = '__all__'