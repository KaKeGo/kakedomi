from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import ToDo
from .serializers import ToDoSerializer

# Create your views here.


@api_view(['GET'])
def todo_list_view(request, *args, **kwargs):
    qs = ToDo.objects.all()
    serializer = ToDoSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def todo_create_view(request, *args, **kwargs):
    serializer = ToDoSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)
