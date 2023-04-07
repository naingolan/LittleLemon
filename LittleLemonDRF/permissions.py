from rest_framework.permissions import BasePermission

class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Manager').exists():
            return True
        else:
            return False
