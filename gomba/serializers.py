from rest_framework import serializers

from .models import products

class productserializer(serializers.Modelserializer):
    class Meta:
        model = products
        fields = '__all__'
