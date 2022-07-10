from django.shortcuts import render
from django.conf import settings

from rest_framework.decorators import api_view, permission_classes
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

@api_view(['POST'])
@permission_classes([IsAdminUser])
def changelog_create_view(request, *args, **kwargs):
    serializer = ChangeLogCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['DELETE', 'POST'])
@permission_classes([IsAdminUser])
def changelog_delete_view(request, changelog_id, *args, **kwargs):
    qs = ChangeLog.objects.filter(id=changelog_id)
    if not qs.exists():
        return Response({'message': 'Something went wrong'}, status=404)
    obj = qs.first()
    obj.delete()
    return Response({'message': 'Change log was removed'}, status=200)
