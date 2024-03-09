from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save



CLIENTS_CHOICES = (
    ("Wagner", "Wagner"),
    ("Desert Ortho", "Desert Ortho"),
    ("Georiga Eye Institute", "Georiga Eye Institute"),
    ("Eyecare Of Atlanta", "Eyecare Of Atlanta"),
    ("Manchester", "Manchester")

)

class Client(models.Model):
    name = models.CharField(choices=CLIENTS_CHOICES, max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(default='default.png')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
     
    def __str__(self) -> str:
        return self.name

class User(AbstractUser):
    first_name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100)
    client = models.ForeignKey(Client, null=True, on_delete=models.RESTRICT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(default='default.png', blank=True, null=True)
    verified = models.BooleanField(default=False, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
     
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
def create_user_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)


# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
    
# def save_client(sender, instance, **kwargs):
#     instance.client.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(create_user_client, sender=User)
# post_save.connect(save_user_profile, sender=User)
# post_save.connect(save_client, sender=User)






