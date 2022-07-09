from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import ToDo
from .serializers import (
ToDoSerializer,
ToDoCreateSerializer,
)

# Create your views here.


@api_view(['GET'])
def todo_list_view(request, *args, **kwargs):
    qs = ToDo.objects.all()
    serializer = ToDoSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def todo_create_view(request, *args, **kwargs):
    serializer = ToDoCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['DELETE', 'POST'])
@permission_classes([IsAdminUser])
def todo_delete_view(request, todo_id, *args, **kwargs):
    qs = ToDo.objects.filter(id=todo_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    obj.delete()
    return Response({'message': 'ToDo was removed'}, status=200)
