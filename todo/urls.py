from django.urls import path

from .views import (
    todo_list_view,
    todo_create_view,
    todo_delete_view,
    todo_update_view,
)

app_name = 'accounts'

urlpatterns = [
   path('', todo_list_view, name='todo'),
   path('create/', todo_create_view, name='create'),
   path('<str:todo_id>/delete/', todo_delete_view, name='delete'),
]
