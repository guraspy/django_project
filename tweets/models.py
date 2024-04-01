from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    content = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    image = models.ImageField(upload_to='tweet_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    no_of_likes = models.IntegerField(default=0)
    
class LikePost(models.Model):
    tweet_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.username