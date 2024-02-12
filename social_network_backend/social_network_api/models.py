from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100,unique=True)


    def __str__(self):
        return f"{self.email} - {self.username} - {self.name}"

class Friendrequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    fromuser = models.ForeignKey(CustomUser, related_name='friend_requests_sent', on_delete=models.CASCADE)
    touser = models.ForeignKey(CustomUser, related_name='friend_requests_received', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    class Meta:
        unique_together = ['fromuser', 'touser']

    def __str__(self):
        return f"{self.from_user} to {self.to_user} - {self.status}"