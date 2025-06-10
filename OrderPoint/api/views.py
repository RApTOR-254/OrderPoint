from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from api.models import Order
from api.serializers import OrderSerializer
from api.permissions import IsOwnerOrReadOnly


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
        user = self.request.user

        return Order.objects.filter(owner=user)

    # Associate Customer with order during "create"
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# @method_decorator(csrf_exempt, name='dispatch') 
class CustomLogoutView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request): #GET method for session based logout (Browser)

        logout(request)

        return Response({"message": "Logged out successfully!"})