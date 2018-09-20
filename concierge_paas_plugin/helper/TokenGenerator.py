from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.conf import settings
from django.contrib import auth

class Generator(auth.models.User):
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create(self, instance=None):
        Token.objects.create(user=instance)