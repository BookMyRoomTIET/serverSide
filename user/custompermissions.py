from rest_framework.permissions import BasePermission

class isStudent(BasePermission):
    def has_permission(self, request, view):
        result = request.user.is_warden
        if result==False:
            return True
        else:
            return False

class isWarden(BasePermission):
    def has_permission(self, request, view):
        result = request.user.is_warden
        return result