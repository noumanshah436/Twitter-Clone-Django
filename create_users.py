# Import necessary modules
# import random
from django.contrib.auth.models import User
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_project.settings.settings')
django.setup()

# Import User model from Django auth


def create_user(username, email, password):
    # Check if the user already exists
    if User.objects.filter(username=username).exists():
        print(f'User with username {username} already exists.')
        return
    # Create a new user
    User.objects.create_user(
        username=username, email=email, password=password)
    print(f'User {username} created successfully.')


# Example usage
if __name__ == '__main__':
    # Replace with actual values
    create_user('john_doe', 'john@example.com', 'password123')


# ********************************************************************

# Import necessary modules

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_project.settings.settings')
django.setup()


def create_users(num_users):
    for i in range(1, num_users + 1):
        username = f'user_{i}'
        email = f'user_{i}@example.com'
        password = f'password{i}'  # Example password generation
        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            print(f'User with username {username} already exists.')
            continue
        # Create a new user
        User.objects.create_user(
            username=username, email=email, password=password)
        print(f'User {username} created successfully.')


# Example usage
if __name__ == '__main__':
    num_users = 5
    create_users(num_users)

# **********************************************************************

# username: user_1
# pass:  password1
