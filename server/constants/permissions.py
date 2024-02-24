from rest_framework.permissions import BasePermission
from django.conf import settings

class InternalIPPermission(BasePermission):
    message = 'Forbidden'

    def has_permission(self, request, view): # type: ignore
        ip_addr = request.META.get('REMOTE_ADDR')
        if ip_addr in settings.INTERNAL_IPS:
            return True
        return False
