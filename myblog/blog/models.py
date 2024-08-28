from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    tags = models.CharField(max_length=200, blank=True)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Subscription(models.Model):
    user = models.ForeignKey(User, related_name='subscribing', on_delete=models.CASCADE)
    subscribed_to = models.ForeignKey(User, related_name='subscribers', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} subscribes to {self.subscribed_to}'
