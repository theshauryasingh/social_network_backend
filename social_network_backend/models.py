from django.db import models

# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)

# class FriendRequest(models.Model):
#     from_user = models.ForeignKey(CustomUser, related_name='from_user', on_delete=models.CASCADE)
#     to_user = models.ForeignKey(CustomUser, related_name='to_user', on_delete=models.CASCADE)
#     status = models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted')], default='pending', max_length=10)
#     created_at = models.DateTimeField(auto_now_add=True)
