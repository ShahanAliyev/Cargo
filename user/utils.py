import random
import string
from django.contrib.auth import get_user_model


def get_user():
    User = get_user_model()
    return User

def generate_unique_digit():
    while True:
        unique_digit = ''.join(random.choices(string.digits, k=8))
        user = get_user()
        if not user.objects.filter(client_code=unique_digit).exists():
            return unique_digit