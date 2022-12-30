from django.db import models

# Create your models here.


class Wallet(models.Model):
    name = models.CharField(max_length=50)
    init_balance = models.IntegerField()

    def __str__(self):
        return f"Wallet {self.name}"
