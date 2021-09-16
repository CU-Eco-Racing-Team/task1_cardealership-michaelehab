from rest_framework import serializers
from .models import Contract

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields =('id', 'start_date', 'end_date', 'supervisor', 'industry', 'number')