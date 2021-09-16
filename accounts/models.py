from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
  #Boolean fields to select the type of the account.
  is_customer = models.BooleanField(default=False)
  is_dealer = models.BooleanField(default=False)
  is_industry = models.BooleanField(default=False)

class Customer(models.Model):
    customer = models.OneToOneField(
      settings.AUTH_USER_MODEL, related_name='customer', on_delete=models.CASCADE)
    ssn = models.IntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return self.customer.username

class Dealer(models.Model):
    dealer = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='dealer', on_delete=models.CASCADE)
    ssn = models.IntegerField()
    phone = models.IntegerField()
    is_owner = models.BooleanField(default=False)
    has_admin_perm = models.BooleanField(default=False)

    def __str__(self):
        return self.dealer.username

class Industry(models.Model):
    industry = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='industry', on_delete=models.CASCADE)
    phone = models.IntegerField()

    def __str__(self):
        return self.industry.username