from django.test import TestCase

# Create your tests here.
import pytest
from rest_framework.test import APITestCase
from .models import Customer, Order

class TestCustomer(APITestCase):
    def test_create_customer(self):
        response = self.client.post('/api/customers/', {'name': 'John Doe', 'code': '123'})
        self.assertEqual(response.status_code, 201)