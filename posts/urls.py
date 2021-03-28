from django.urls import re_path, path
from django.contrib import admin
from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
)

app_name='posts'

urlpatterns = [
    re_path(r'^$',post_list, name='list'),
    re_path(r'^create/$',post_create, name='list'),
    re_path(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
]
