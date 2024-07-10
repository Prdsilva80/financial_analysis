from rest_framework import serializers
from core.models import StockData

class StockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockData
        fields = '__all__'
