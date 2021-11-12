from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Listing, Review, Member
from .serializers import ListingSerializer, ReviewSerializer, MemberSerializer
from django.contrib.auth import get_user_model
from authentication.serializers import RegistrationSerializer
from django.shortcuts import redirect
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

User = get_user_model()


# Listing queries
# Get all
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_listings(request):
    listings = Listing.objects.all()
    serializer = ListingSerializer(listings, many=True)
    return Response(serializer.data)


# Get by current user
@api_view(['GET'])
@permission_classes([AllowAny])
def get_current_users_listings(request):
    listings = Listing.objects.get(user_id=request.user.id)
    serializer = ListingSerializer(listings)
    return Response(serializer.data)


# Get by user id
@api_view(['GET'])
@permission_classes([AllowAny])
def get_users_listings_by_id(request, user_id):
    user = User.objects.get(pk=user_id)
    listings = Listing.objects.get(user_id=user.id)
    serializer = ListingSerializer(listings)
    return Response(serializer.data)


# Post
@api_view(['POST'])
@permission_classes([AllowAny])
def post_listing(request):
    if request.method == 'POST':
        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Put by user id
@api_view(['PUT'])
@permission_classes([AllowAny])
def put_listing(request, user_id):
    listing = Listing.objects.get(user_id=user_id)
    serializer = ListingSerializer(listing, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete by user id
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_listing(request, user_id):
    listing = Listing.objects.get(user_id=user_id)
    listing.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Review queries
# Post review on lister's id
@api_view(['POST'])
@permission_classes([AllowAny])
def post_review(request):
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
# Gets members
@api_view(['GET'])
@permission_classes([AllowAny])
def get_members(request, listers_id):
    members = Member.objects.select_related(
        'user').filter(listing=listers_id)
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)


# Post member to listing
@api_view(['POST'])
@permission_classes([AllowAny])
def post_member(request):
    if request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Post Stripe checkout
@api_view(['POST'])
@permission_classes([AllowAny])
def post_checkout(request):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1Juv2yDG5C4sOYL1t3pM5ylx',
                    'quantity': 1,
                },
            ],
            payment_method_types=['card'],
            mode='payment',
            success_url='http://localhost:3000/?success=true&session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://localhost:3000/?canceled=true',
        )
        return redirect(checkout_session.url)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
