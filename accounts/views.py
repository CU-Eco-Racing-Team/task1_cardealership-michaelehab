from django.shortcuts import render
from rest_framework.response import Response
from rest_auth.registration.views import RegisterView
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from accounts.serializers import (
    DealerCustomRegistrationSerializer, CustomerCustomRegistrationSerializer,
    IndustryCustomRegistrationSerializer, DealerSerializer, CustomerSerializer, IndustrySerializer,
    IndustrySerializer
)
from .models import Dealer, Customer, Industry

#Allow Owner to pass his position to a dealer or give him admin permissions
class isUserOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_dealer:
            if request.user.dealer.is_owner:
                return True
        return False


#Custom Registration Views
class DealerRegistrationView(RegisterView):
    serializer_class = DealerCustomRegistrationSerializer

class CustomerRegistrationView(RegisterView):
    serializer_class = CustomerCustomRegistrationSerializer

class IndustryRegistrationView(RegisterView):
    serializer_class = IndustryCustomRegistrationSerializer

#Views for showing a list of each type of users
class DealerList(viewsets.ReadOnlyModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer

class CustomerList(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class IndustryList(viewsets.ReadOnlyModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

@api_view(['GET'])
@permission_classes((isUserOwner,))
def pass_position(request, id):
    try:
        dealer = Dealer.objects.get(pk=id)
        dealer.is_owner = True
        dealer.save()
        owner = Dealer.objects.get(pk=request.user.dealer.id)
        owner.is_owner = False
        owner.save()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((isUserOwner,))
def give_admin_permissions(request, id):
    try:
        dealer = Dealer.objects.get(pk=id)
        dealer.has_admin_perm = True
        dealer.save()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)