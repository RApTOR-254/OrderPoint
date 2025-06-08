from api.models import Customer, Order

from rest_framework import serializers


# Order serializer
class OrderSerializer(serializers.ModelSerializer):
    # Add associated customer as owner
    owner = serializers.ReadOnlyField(source="owner.name")

    class Meta:
        model = Order
        fields = ["id", "item", "amount", "owner"]


# Customer (User) serializer
class CustomerSerializer(serializers.ModelSerializer):
    #Orders associated with customer added explicitly because of reverse relationship
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())
    
    class Meta:
        model = Customer
        fields = ["id", "name", "email", "sub", "phone_number", "orders"]