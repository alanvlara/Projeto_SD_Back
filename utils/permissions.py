from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view or edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        # Always allow GET requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Logs para depuração

        # Write permissions are only allowed to the owner of the activity
        return obj.usuario == request.user
    
class IsOwnerOrReadOnlyUser(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view or edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        # Always allow GET requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Logs para depuração

        # Write permissions are only allowed to the owner of the activity
        return obj == request.user