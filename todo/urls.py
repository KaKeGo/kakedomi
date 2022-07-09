from django.urls import path

from .views import (
    todo_list_view,
    todo_create_view,
)

app_name = 'accounts'

urlpatterns = [
   path('', todo_list_view, name='todo'),
   path('create/', todo_create_view, name='create'),
]
