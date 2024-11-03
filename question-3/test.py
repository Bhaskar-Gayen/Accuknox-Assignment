from users.models import UserProfile


try:
    user = UserProfile.objects.create(
        username="testuser", email="testuser@example.com")
except ValueError as e:
    print(f"Caught an exception: {e}")

user_exists = UserProfile.objects.filter(username="testuser").exists()
print(f"Was the user saved? {user_exists}")
