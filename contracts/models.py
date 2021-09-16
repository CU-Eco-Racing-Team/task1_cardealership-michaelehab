from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import Industry, Dealer

# Create your models here.
class Contract(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    supervisor = models.ForeignKey(Dealer, related_name='contract_supervisor',  on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, related_name='contract_industry', on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return self.industry
