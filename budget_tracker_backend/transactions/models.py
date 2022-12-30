from django.db import models

# Create your models here.


class Transaction(models.Model):
    notes = models.CharField(max_length=200)
    amount = models.IntegerField()
    category = models.CharField(max_length=100)
    currency = models.CharField(max_length=3)
    date = models.DateTimeField()
