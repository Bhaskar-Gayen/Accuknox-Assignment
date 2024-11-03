# Django Signal Thread Execution Demonstration

Yes, Django signals run in the same thread as the caller by default. To prove this, We can do same example as previos with minor changes post_save signal on a receving function, then we find both the caller and the signal receiver thread id.

This example demonstrates that **Django signals run in the same thread as the caller by default**.

## Overview

In this example:

1. A `UserProfile` instance is created, which triggers the `post_save` signal.
2. Both the caller and the signal receiver print their thread IDs.
3. Since both IDs are the same, this confirms that the signal executes in the same thread as the caller.

## Code Implementation

### 1. Signal Definition

Define a `post_save` signal in `signals.py` to print the thread ID of the signal receiver.

```python
# users/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
from .models import UserProfile

@receiver(post_save, sender=UserProfile)
def welcome_user(sender, instance, created, **kwargs):
    if created:
        print(f"[Signal Receiver] Thread ID: {threading.get_ident()}")
        print(f"Welcome, {instance.username}!")
```

$ python.exe manage.py shell

from users.models import UserProfile
import threading
print(f"[Caller] Thread ID: {threading.get_ident()}")
[Caller] Thread ID: 20204
user = UserProfile.objects.create(username="sana", email="sana@example.com")
[Signal Receiver] Thread ID: 20204
Welcome, sana!
