from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp import devices_for_user, login
from rest_framework import permissions
import json


def get_user_totp_device( user, confirmed=None):
    devices = devices_for_user(user, confirmed=confirmed)
    for device in devices:
        if isinstance(device, TOTPDevice):
            return device

def is_verified(request, false_on_no_device= False ):
    user = request.user
    print(user.last_verified_session, "==", request.headers['unique-id'])
    if user.last_verified_session == request.headers['unique-id']:
        return True
    device = get_user_totp_device(user, confirmed= True)
    if (not device) and  (not false_on_no_device):
        return True
    return False

def login_user(request, device):
    user = request.user
    registered_device = get_user_totp_device(user, True)
    if device == registered_device:
        user.last_verified_session = request.headers['unique-id']
        user.save()
        return True
    return False
 
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class IsVerified(permissions.BasePermission):

    message = 'User Not Verified'

    def has_permission(self, request, view):
        return is_verified(request)


