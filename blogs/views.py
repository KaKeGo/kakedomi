from django.shortcuts import render
from django.conf import settings

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView

from .models import Category, Blog
from .serializers import (
CategorySerializer,
CategoryCreateSerializer,

BlogSerializer,
BlogCreateSerializer,
)

# Create your views here.


@api_view(['GET'])
def category_view(request):
    qs = Category.objects.all()
    serializer = CategorySerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([IsAdminUser])
def category_create_view(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['GET'])
def blog_view(request):
    qs = Blog.objects.all()
    serializer = BlogSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def blog_create_view(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(
            author=request.user
        )
        return Response(serializer.data, status=201)
    return Response({}, status=400)
