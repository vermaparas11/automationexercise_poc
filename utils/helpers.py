import random
import string

def random_string(length=6):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_random_user():
    rand = random_string()
    return {
        "name": f"User_{rand}",
        "email": f"user_{rand}@testmail.com",
        "password" : "Test@123"
    }