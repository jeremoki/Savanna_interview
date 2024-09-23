from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Customer, Order

class TestCustomer(APITestCase):

    def test_create_customer(self):
        data = {'name': 'John Doe', 'code': '123'}
        response = self.client.post('/api/customers/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['code'], data['code'])
        self.assertTrue(Customer.objects.filter(name=data['name'], code=data['code']).exists())

    def test_create_customer_invalid_data(self):
        data = {'name': '', 'code': ''}
        response = self.client.post('/api/customers/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)
        self.assertIn('code', response.data)

    def test_get_customers(self):
        Customer.objects.create(name='John Doe', code='123')
        response = self.client.get('/api/customers/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'John Doe')
        self.assertEqual(response.data[0]['code'], '123')

    def test_get_customer_detail(self):
        customer = Customer.objects.create(name='John Doe', code='123')
        response = self.client.get(f'/api/customers/{customer.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John Doe')
        self.assertEqual(response.data['code'], '123')

    def test_update_customer(self):
        customer = Customer.objects.create(name='John Doe', code='123')
        data = {'name': 'Jane Doe', 'code': '456'}
        response = self.client.put(f'/api/customers/{customer.id}/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Jane Doe')
        self.assertEqual(response.data['code'], '456')

    def test_delete_customer(self):
        customer = Customer.objects.create(name='John Doe', code='123')
        response = self.client.delete(f'/api/customers/{customer.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Customer.objects.filter(id=customer.id).exists())
