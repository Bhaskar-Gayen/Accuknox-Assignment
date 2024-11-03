from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
import time


@receiver(post_save, sender=UserProfile)
def welcome_user(sender, instance, created, **kwargs):
    print('signal received')
    time.sleep(2)  # Simulate a delay to observe synchronous behavior
    if created:
        print(f"Welcome, {instance.username}!")

    print("signal processed")
