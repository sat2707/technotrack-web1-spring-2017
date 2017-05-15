# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import BlogsList, BlogView, PostView, UpdateBlog, CreateBlog, UpdatePost, PostCommentsView, PostLikeView


urlpatterns = [
    url(r'^blogs/$', BlogsList.as_view(), name="allblogs"),
    url(r'^blogs/new/$', login_required(CreateBlog.as_view()), name="createblog"),
    url(r'^blogs/(?P<pk>\d+)/edit/$', UpdateBlog.as_view(), name="editblog"),
    url(r'^blogs/(?P<pk>\d+)/$', BlogView.as_view(), name="oneblog"),
    url(r'^posts/(?P<pk>\d+)/$', PostView.as_view(), name="onepost"),
    url(r'^posts/(?P<pk>\d+)/comments/$', PostCommentsView.as_view(), name="onepostcomments"),
    url(r'^posts/(?P<pk>\d+)/like/$', login_required(PostLikeView.as_view()), name="onepostlike"),
    url(r'^posts/(?P<pk>\d+)/edit/$', login_required(UpdatePost.as_view()), name="editpost"),
]