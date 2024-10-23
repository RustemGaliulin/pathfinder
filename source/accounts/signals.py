from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import CustomUser


@receiver(post_save, sender=CustomUser)
def create_jwt_token(sender, instance=None, created=False, **kwargs):
    if created:
        refresh = RefreshToken.for_user(instance)
        print(f'JWT Token created for user {instance.username}: {str(refresh.access_token)}')
