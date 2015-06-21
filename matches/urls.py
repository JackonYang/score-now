#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('matches.views',
    url(r'^$', 'match_list', name='match_list'),
    url(r'^europe/(\d+)$', 'europe', name='europe'),
)
