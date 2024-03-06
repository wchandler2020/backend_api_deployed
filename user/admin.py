from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


from .models import User, Profile, Client

# Register your models here.
class UserAdmin(DjangoUserAdmin):
    list_display = ['username', 'email', 'client']
    fieldsets = DjangoUserAdmin.fieldsets + (('User Info', {"fields": ["client", "phone_number"]}),)


    list_editable = ['client']

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user', 'first_name', 'last_name', 'verified']
    
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name']
    exclude = ('first_name', 'last_name')


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Client, ClientAdmin)
