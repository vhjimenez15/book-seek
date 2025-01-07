from rest_framework.permissions import BasePermission
from django.contrib.auth.models import AnonymousUser


class AllowAny(BasePermission):
    def has_permission(self, request, view):
        return True


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return False
        return bool(request.user and request.user["is_authenticated"])
