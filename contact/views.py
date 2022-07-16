from django.shortcuts import render
from django.conf import settings

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import Contact, ContactMessage
from .serializers import (
ContactSerializer,
ContactMessageSerializer,
)

# Create your views here.


@api_view(['GET'])
def contact_view(request):
    qs = Contact.objects.all()
    serializer = ContactSerializer(qs, many=True)
    return Response(serializer.data)
