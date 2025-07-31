from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsEditor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'editor'

class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'viewer'

class IsAdminOrEditor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'editor']

class WebsitePermission(BasePermission):
   

    def has_permission(self, request, view):
        role = request.user.role
        if role == 'admin':
            return True
        elif role == 'editor':
            if request.method in SAFE_METHODS or request.method in ['POST', 'PUT', 'PATCH']:
                return True
            return False
        elif role == 'viewer':
            return request.method in SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        elif request.user.role == 'editor':
            return obj.user == request.user
        elif request.user.role == 'viewer':
            return request.method in SAFE_METHODS
        return False
