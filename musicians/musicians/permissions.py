from rest_framework import permissions


class IsAuthorOrStaffOrReadOnly(permissions.BasePermission):
    """Allow to change the data of musician if it's author or staff else read only"""
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.post_author == request.user or request.user.is_staff


class IsStaffOrReadyOnly(permissions.BasePermission):
    """Allow to change the data if it's staff else read only"""
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff
