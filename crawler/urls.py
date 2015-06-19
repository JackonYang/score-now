#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('crawler.views',
    url(r'^$', 'match_list', name='match_list'),
)
