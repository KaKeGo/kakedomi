from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ToDo
from .serializers import ToDoSerializer

# Create your views here.


@api_view(['GET'])
def todo_list_view(request, *args, **kwargs):
    qs = ToDo.objects.all()
    serializer = ToDoSerializer(qs, many=True)
    return Response(serializer.data)
