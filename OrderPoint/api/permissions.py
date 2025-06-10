from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Permission to only allow the owner of an order to edit it"""
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user