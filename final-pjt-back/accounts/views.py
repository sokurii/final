from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators - 함수를 꾸며주는 함수
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ProfileSerializer, CustomUserSerializer
from .models import Profile

# Create your views here.

@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_profile(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request, username):
    User = get_user_model()
    customUser = User.objects.get(username=username)
    serializer = CustomUserSerializer(customUser)
    return Response(serializer.data) 