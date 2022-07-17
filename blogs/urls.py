from django.urls import path

from .views import (
category_view,
category_create_view,
category_delete_view,
CategoryUpdateView,

blog_view,
blog_create_view,
blog_delete_view,
BlogUpdateView,
)

app_name = 'blogs'

urlpatterns = [
    #Category
    path('category/', category_view, name='category'),
    path('category/create/', category_create_view, name='category_create'),
    path('category/<slug:slug>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<slug:slug>/delete/', category_delete_view, name='category_delete'),
    #Blog
    path('', blog_view, name='blog'),
    path('create/', blog_create_view, name='blog_create'),
    path('create/<slug:slug>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('create/<slug:slug>/delete/', blog_delete_view, name='blog_delete'),
]
