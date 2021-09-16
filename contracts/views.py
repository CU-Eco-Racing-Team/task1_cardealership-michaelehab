from django.shortcuts import render
from rest_framework import viewsets
from .models import Contract
from .serializers import ContractSerializer

class ContractView(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    #Restrict Contract modification
    http_method_names = ['get', 'post']