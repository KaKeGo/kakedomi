from django.urls import path

from .views import (
    changelog_list_view,
    changelog_create_view,
    changelog_delete_view,
)

app_name = 'changelog'

urlpatterns = [
    path('', changelog_list_view, name='changelog'),
    path('create/', changelog_create_view, name='create'),
    path('<str:changelog_id>/delete/', changelog_delete_view, name='delete'),
]
