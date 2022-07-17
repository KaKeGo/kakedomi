from django.urls import path

from .views import (
category_view,
category_create_view,

blog_view,
blog_create_view,
)

app_name = 'blogs'

urlpatterns = [
    #Category
    path('category/', category_view, name='category'),
    path('category/create/', category_create_view, name='category_create'),
    #Blog
    path('', blog_view, name='blog'),
    path('create/', blog_create_view, name='blog_create'),
]
