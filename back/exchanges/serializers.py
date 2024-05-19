from rest_framework import serializers
from .models import Current, ExchangeRate

class CurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Current
        fields = '__all__'
        
        
class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = '__all__'