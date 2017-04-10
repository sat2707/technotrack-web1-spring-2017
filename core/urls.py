# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from .views import MainPage


urlpatterns = [
    url(r'^$', MainPage.as_view(), name='mainpage'),
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
]
