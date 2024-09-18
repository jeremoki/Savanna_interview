# myapp/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        order = super().create(request, *args, **kwargs)
        send_sms(order.customer.code, f'Your order {order.item} is ready!')
        return Response(order.data, status=status.HTTP_201_CREATED)

def send_sms(phone_number, message):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=phone_number,
        from_='your_twilio_number',
        body=message
    )