from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api import views

router = DefaultRouter()

router.register(r'orders', views.OrderViewSet, basename="order")
router.register(r'customers', views.CustomerViewset, basename="customer")

urlpatterns = [
    path('', include(router.urls))
]