from django.conf.urls import url
from django.contrib import admin
from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    post_signin,
    post_signup,
    post_logout,
)

appname = 'posts'

urlpatterns = [
    url(r'^$', post_list, name = "home"),
    url(r'^create/$', post_create, name='create'),
    url(r'^signin/$', post_signin, name='signin'),
    url(r'^signup/$', post_signup, name='signup'),
    url(r'^logout/$', post_logout, name='logout'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
]
