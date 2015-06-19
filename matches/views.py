#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response


def match_list(request):
    return render_to_response('home.html', RequestContext(request))
