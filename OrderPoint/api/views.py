from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from api.models import Order, Customer
from api.serializers import OrderSerializer, CustomerSerializer
from api.permissions import IsOwnerOrReadOnly
from api.sms_service import send_sms


class OrderViewSet(viewsets.ModelViewSet):
    """
    Automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions
    """
    serializer_class = OrderSerializer
    permission_classes = [
        IsAuthenticated, #Only authenticated Customers can perform CRUDE
        IsOwnerOrReadOnly, #Only the owner of an order can edit it
    ]

    def get_queryset(self):
        user = self.request.user #user is the current user

        return Order.objects.filter(owner=user) #List only Order instacen associated with user.

    #Associate Customer with order during "create" and then
    # Notify the user via sms 
    def perform_create(self, serializer):
        #args:
        user = self.request.user
        message = f'Dear {user.name}, your order has been submitted successfully! We\'ll notify you when the shipment begins. Thank you for shopping with us'
        recipients = [f'{user.phone_number}']
        sender_id = None #for development

        try:
            serializer.save(owner=user) 
            result = send_sms(message, recipients, sender_id) 
            return Response(result)
        except Exception as e:
            return {"error": str(e)}
        
class CustomerViewset(viewsets.ReadOnlyModelViewSet):
    """List and Retrieve Customer instances"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# @method_decorator(csrf_exempt, name='dispatch') 
class CustomLogoutView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request): #GET method for session based logout (Browser)

        logout(request)

        return Response({"message": "Logged out successfully!"})