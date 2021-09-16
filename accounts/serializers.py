from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from accounts.models import User, Dealer, Customer, Industry
from cars.serializers import DealSerializer

class DealerCustomRegistrationSerializer(RegisterSerializer):
    dealer = serializers.PrimaryKeyRelatedField(read_only=True)
    ssn = serializers.IntegerField(required=True)
    phone = serializers.IntegerField(required=True)
    is_owner = serializers.BooleanField(default=False)
    has_admin_perm = serializers.BooleanField(default=False)
    
    def get_cleaned_data(self):
            data = super(DealerCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'ssn' : self.validated_data.get('ssn', ''),
                'phone' : self.validated_data.get('phone', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(DealerCustomRegistrationSerializer, self).save(request)
        user.is_dealer = True
        user.save()
        dealer = Dealer(dealer=user, ssn=self.cleaned_data.get('ssn'), 
                phone=self.cleaned_data.get('phone'))
        dealer.save()
        return user


class CustomerCustomRegistrationSerializer(RegisterSerializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    ssn = serializers.IntegerField(required=True)
    phone = serializers.IntegerField(required=True)
    
    def get_cleaned_data(self):
            data = super(CustomerCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'ssn' : self.validated_data.get('ssn', ''),
                'phone' : self.validated_data.get('phone', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(CustomerCustomRegistrationSerializer, self).save(request)
        user.is_customer = True
        user.save()
        customer = Customer(customer=user, ssn=self.cleaned_data.get('ssn'), 
                phone=self.cleaned_data.get('phone'))
        customer.save()
        return user

class IndustryCustomRegistrationSerializer(RegisterSerializer):
    industry = serializers.PrimaryKeyRelatedField(read_only=True)
    phone = serializers.IntegerField(required=True)
    
    def get_cleaned_data(self):
            data = super(IndustryCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'phone' : self.validated_data.get('phone', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(IndustryCustomRegistrationSerializer, self).save(request)
        user.is_industry = True
        user.save()
        industry = Industry(industry=user, phone=self.cleaned_data.get('phone'))
        industry.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class DealerSerializer(serializers.ModelSerializer):
    dealer_data = UserSerializer(source='dealer', read_only = True)
    class Meta:
        model = Dealer
        fields = ('id', 'ssn', 'phone', 'is_owner', 'dealer_data')

class CustomerSerializer(serializers.ModelSerializer):
    customer_data = UserSerializer(source='customer', read_only = True)
    customer_deals = DealSerializer(read_only=True, many=True)
    class Meta:
        model = Dealer
        fields = ('id', 'ssn', 'phone', 'customer_data', 'customer_deals')

class IndustrySerializer(serializers.ModelSerializer):
    industry_data = UserSerializer(source='industry', read_only = True)
    class Meta:
        model = Dealer
        fields = ('id', 'phone', 'industry_data')