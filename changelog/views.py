from django.shortcuts import render
from django.conf import settings

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import ChangeLog
from .serializers import (
ChangeLogSerializer,
ChangeLogCreateSerializer
)

# Create your views here.


@api_view(['GET'])
def changelog_list_view(request, *args, **kwargs):
    qs = ChangeLog.objects.all()
    serializer = ChangeLogSerializer(qs, many=True)
    return Response(serializer.data)
