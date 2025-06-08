from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from api.managers import CustomerManager

class Customer(AbstractBaseUser):
    # Customer Identification
    name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, null=False, blank=False, max_length=255)
    sub = models.CharField(blank=False, null=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    # Permissions
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["sub"]
    USERNAME_FIELD = "email"

    objects = CustomerManager()

    def __str__(self):
        return f"{self.name} => {self.sub}"


class Order(models.Model):
    item = models.CharField(max_length=50, null=False, blank=False)
    amount = models.IntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    # Cusomer details
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
