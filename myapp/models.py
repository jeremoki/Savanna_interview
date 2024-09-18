from django.db import models
from django.contrib.auth.models import User
User.objects.create_user('testuser', 'testuser@example.com', 'testpassword')


class Customer(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    class Meta:
        app_label = 'myapp'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    amount = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'myapp'
