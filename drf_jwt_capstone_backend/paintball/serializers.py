from rest_framework import serializers
from .models import Listing, Review, Member


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'start_time', 'end_time', 'start_date',
                  'user', 'name', 'price', 'product_id', 'price_id']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'content', 'rating', 'user']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'listing', 'user']
