# permissions.py

from rest_framework import permissions


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only authenticated users to edit or delete.
    """

    def has_permission(self, request, view):
        # Allow anyone to view (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Otherwise, check if the user is authenticated
        return request.user and request.user.is_authenticated
