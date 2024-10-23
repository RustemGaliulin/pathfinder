from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, verbose_name='email address', null=False, blank=False)
    username = models.CharField(max_length=255, verbose_name='username', null=False, blank=False, unique=True)
    password = models.CharField(max_length=255, verbose_name='password', null=False, blank=False)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

