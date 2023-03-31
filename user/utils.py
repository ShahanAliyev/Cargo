import random
import string

def generate_unique_digit():
    return ''.join(random.choices(string.digits, k=8))