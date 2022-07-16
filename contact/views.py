from django.shortcuts import render
from django.conf import settings

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView

from .models import Contact, ContactMessage
from .serializers import (

ContactSerializer,
ContactCreateSerializer,

ContactMessageSerializer,
ContactMessageCreateSerializer,
)

# Create your views here.


@api_view(['GET'])
def contact_view(request):
    qs = Contact.objects.all()
    serializer = ContactSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def contact_create_view(request):
    serializer = ContactCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['DELETE', 'GET', 'POST'])
@permission_classes([IsAdminUser])
def contact_delete_view(request, slug, *args, **kwargs):
    qs = Contact.objects.filter(slug=slug)
    if not qs.exists():
        return Response({'message': 'Something went wrong'}, status=404)
    obj = qs.first()
    obj.delete()
    return Response({'message': 'Contact content was removed'}, status=200)

class ContactUpdateView(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'slug'

@api_view(['GET'])
def contact_message_view(request):
    qs = ContactMessage.objects.all()
    serializer = ContactMessageSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def contact_create_message_view(request):
    serializer = ContactMessageCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(
            postman=request.user
                        )
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['DELETE', 'GET', 'POST'])
@permission_classes([IsAuthenticated])
def contact_message_delete_view(request, slug, *args, **kwargs):
    qs = ContactMessage.objects.filter(slug=slug)
    if not qs.exists():
        return Response({'message': 'Something want wrong'}, status=404)
    obj = qs.first()
    obj.delete()
    return Response({'message': 'Message was removed'}, status=200)

class ContactUpdateMessageView(UpdateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    lookup_field = 'slug'
