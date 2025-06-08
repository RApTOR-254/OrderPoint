from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api import views

router = DefaultRouter()

router.register(r'orders', views.OrderViewSet, basename="order")

urlpatterns = [
    path('', include(router.urls))
]