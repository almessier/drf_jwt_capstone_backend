from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Listing(models.Model):
    user = models.ManyToManyField(User)
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_date = models.DateField()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    rating = models.IntegerField()
