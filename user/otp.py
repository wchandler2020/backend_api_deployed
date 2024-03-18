from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp import devices_for_user, login
from rest_framework import permissions


def get_user_totp_device( user, confirmed=None):
    devices = devices_for_user(user, confirmed=confirmed)
    for device in devices:
        if isinstance(device, TOTPDevice):
            return device

def is_verified(request, false_on_no_device= False ):
    user = request.user
    
    if 'is_verified' in request.session:
        return True
    device = get_user_totp_device(user, confirmed= True)
    if (not device) and  (not false_on_no_device):
        return True
    return False

def login_user(request, device):
    user = request.user
    registered_device = get_user_totp_device(user, True)
    if device == registered_device:
        request.session['is_verified'] = True 
    return False
 


class IsVerified(permissions.BasePermission):

    message = 'User Not Verified'

    def has_permission(self, request, view):
        return is_verified(request)