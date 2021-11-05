from rest_framework import serializers
from .models import Listing, Review


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'start_time', 'end_time', 'start_date', 'user_id']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'content', 'rating', 'user_id']
