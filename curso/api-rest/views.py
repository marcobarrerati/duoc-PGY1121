from rest_framework import viewsets
from customer.models import Customer
from customer.serializers import CustomerSerializer


class CustomViewSet(viewsets.ModelViewSet):
    model = Customer
    queryset = Customer.object.all()
    serializer_class = CustomerSerializer
