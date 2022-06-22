from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    created = models.DateTimeField(auto_now_add=True)
    Id = models.AutoField(primary_key=True, unique=True, 
                                             editable=False)

    def __str__(self):
        return str(self.username)
    

def profileUpdated(sender, instance, created, **kwargs):
    print('Profile Saved!')
    print('Instance:', instance)
    print('Created:', created)

def deleteUser(sender, instance, **kwargs):
    print('Deleting user...')
    
 
# post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(deleteUser, sender=Profile)