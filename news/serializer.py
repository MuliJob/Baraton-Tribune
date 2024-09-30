from rest_framework import serializers
from .models import BaratonMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaratonMerch
        fields = ('name', 'description', 'price')