from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_date = models.DateField()
    product_id = models.CharField(max_length=250)
    price_id = models.CharField(max_length=250)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    rating = models.IntegerField()


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
