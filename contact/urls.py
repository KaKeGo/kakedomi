from django.urls import path

from .views import (

    contact_view,
    contact_create_view,
    contact_delete_view,

    contact_message_view,
    contact_create_message_view,
    contact_message_delete_view,
)

app_name = 'contact'

urlpatterns = [
    #Contact
    path('', contact_view, name='contact'),
    path('create/', contact_create_view, name='contact_create'),
    path('<slug:slug>/delete/', contact_delete_view, name='contact_delete'),
    #Contact messages
    path('messages/', contact_message_view, name='contact_messages'),
    path('messages/create/', contact_create_message_view, name='messages_create'),
    path('messages/<slug:slug>/delete/', contact_message_delete_view, name='messages_delete'),
]