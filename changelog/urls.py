from django.urls import path

from .views import (
    changelog_list_view,
)

app_name = 'changelog'

urlpatterns = [
    path('', changelog_list_view, name='changelog'),
]
