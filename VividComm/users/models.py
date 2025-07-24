from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields here that you want for your user
    # For a chat app, a phone number and profile picture are common.
    phone_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)

    # You can add related_name arguments to avoid clashes with auth.User
    # For example, if you have groups or user_permissions relations in the future
    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='custom_users',
    #     blank=True,
    #     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    #     verbose_name='groups',
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='custom_users',
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     verbose_name='user permissions',
    # )

    def __str__(self):
        return self.username