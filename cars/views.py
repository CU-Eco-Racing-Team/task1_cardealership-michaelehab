from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Car, Deal
from .serializers import CarSerializer, DealSerializer

#Allow Owner and Dealers with administrative features to edit details
class CanEditDetails(permissions.BasePermission):
    def has_permission(self, request, view):
        return True
        
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.is_dealer:
            if request.user.dealer.is_owner or request.user.dealer.has_admin_perm:
                return True
        return False

class CarView(viewsets.ModelViewSet):   
    permission_classes = [CanEditDetails]
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class DealView(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    #Restrict Contract modification
    http_method_names = ['get', 'post']