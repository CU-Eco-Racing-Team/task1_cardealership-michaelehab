from django.db import models
from accounts.models import Industry, Customer

class Car(models.Model):
    car_model = models.CharField(max_length=100)
    price = models.FloatField()
    industry = models.ForeignKey(Industry, related_name='car_industry', on_delete=models.CASCADE)

    def __str__(self):
        return self.car_model

PAYMENT_METHODS =( 
    ("1", "Cash"), 
    ("2", "Installment"),
)

class Deal(models.Model):
    car = models.ForeignKey(Car, related_name='car_deals', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='customer_deals', on_delete=models.CASCADE)
    plate = models.CharField(max_length=10)
    payment = models.CharField(max_length=1, choices=PAYMENT_METHODS)

    def __str__(self):
        return self.plate