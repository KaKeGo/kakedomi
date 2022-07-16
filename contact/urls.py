from django.urls import path

from .views import (
    contact_view,
    contact_message_view,
)

app_name = 'contact'

urlpatterns = [
    #Contact
    path('', contact_view, name='contact'),
    #Contact messages
    path('messages/', contact_message_view, name='contact_messages'),
]