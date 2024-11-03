from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
import threading


@receiver(post_save, sender=UserProfile)
def welcome_user(sender, instance, created, **kwargs):

    print(f"[Signal Receiver] Thread ID: {threading.get_ident()}")

    if created:
        print(f"welcome {instance.username}!")
