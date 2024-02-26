from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Tweet(models.Model):
    content = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    image = models.ImageField(upload_to='tweet_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
