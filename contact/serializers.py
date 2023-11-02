from rest_framework import serializers
from .models import Suppliers
from .models import Customers

class Suppliers_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Suppliers
        fields=('__all__')


class Customers_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields=('__all__')