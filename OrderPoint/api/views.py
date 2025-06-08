from rest_framework import viewsets

from api.models import Order
from api.serializers import OrderSerializer
# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    """
    Automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # Associate Customer with order during "create"
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)