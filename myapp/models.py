from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    amount = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item
