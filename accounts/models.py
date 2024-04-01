from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(blank=True, null=True)
    surname = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images/', default='blank-profile-picture.png')
    
    def __str__(self) -> str:
        return self.user.username