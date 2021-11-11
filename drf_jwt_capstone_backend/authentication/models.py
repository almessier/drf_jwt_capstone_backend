from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


def upload_path(instance, filename):
    return '/'.join(['avatars', str(instance.id), filename])


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=250, default='123 E Pine Dr')
    phone_number = models.CharField(max_length=10, default=0)
    is_listed = models.BooleanField(default=False)
    lat = models.DecimalField(max_digits=23, decimal_places=20, default=0)
    lng = models.DecimalField(max_digits=23, decimal_places=20, default=0)
    avatar = models.ImageField(blank=True, null=True, upload_to=upload_path)
