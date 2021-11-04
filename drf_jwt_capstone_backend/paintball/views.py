from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Listing, Review, Member
from .serializers import ListingSerializer, ReviewSerializer, MemberSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


# Listing queries
# Get all
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_listings(request):
    listings = Listing.objects.all()
    serializer = ListingSerializer(listings, many=True)
    return Response(serializer.data)


# Get by user id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users_listings(request):
    listings = Listing.objects.filter(user_id=request.user.id)
    serializer = ListingSerializer(listings)
    return Response(serializer.data)


# Post
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_listing(request):
    if request.method == 'POST':
        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Put by user id
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def put_listing(request, user_id):
    listing = Listing.objects.get(user_id=user_id)
    serializer = ListingSerializer(listing, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete by user id
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_listing(request):
    if request.method == 'DELETE':
        listing = Listing.objects.filter(user_id=request.user.id)
        listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Review queries
# Post review on lister's id
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_review(request):
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get all reviews by lister's id
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_listers_reviews(request, listers_id):
    reviews = Review.objects.filter(user_id=listers_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


# Get all reviews
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_reviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


# Member queries
# Post member AKA join listing
# Gets members
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_members(request, user_id, listers_id):
    members = Member.get.all(listing_id=listers_id)
    member_users = members.get.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_member(request):
    if request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
