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

@api_view(['DELETE', 'GET', 'POST'])
@permission_classes([IsAdminUser])
def category_delete_view(request, slug, *args, **kwargs):
    qs = Category.objects.filter(slug=slug)
    if not qs.exists():
        return Response({'message': 'Something went wrong'}, status=404)
    obj = qs.first()
    obj.delete()
    return Response({'message': 'Category content was removed'})

class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = IsAdminUser

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

@api_view(['DELETE', 'GET', 'POST'])
@permission_classes([IsAdminUser])
def blog_delete_view(request, slug, *args, **kwargs):
    qs = Blog.objects.filter(slug=slug)
    if not qs.exists():
        return Response({'message': 'Something went wrong'}, status=404)
    obj = qs.first()
    obj.delete()
    return Response({'message': 'Blog content was removed'}, status=200)

class BlogUpdateView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    permission_classes = IsAdminUser
