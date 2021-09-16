from rest_framework import serializers
from .models import Car, Deal

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields =('id', 'car', 'customer','plate', 'payment')

class CarSerializer(serializers.ModelSerializer):
    car_deals = DealSerializer(read_only=True, many=True)
    class Meta:
        model = Car
        fields =('id', 'car_model', 'industry', 'price', 'car_deals')