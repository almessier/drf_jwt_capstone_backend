from django.contrib.auth import get_user_model
from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


# Get all users
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_users(request):
    users = User.objects.all()
    serializer = RegistrationSerializer(users, many=True)
    return Response(serializer.data)


# Get user by id
@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_by_id(request, user_id):
    user = User.objects.filter(pk=user_id)
    serializer = RegistrationSerializer(user, many=True)
    return Response(serializer.data)


# Update user
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def put_user(request):
    if request.method == 'PUT':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
