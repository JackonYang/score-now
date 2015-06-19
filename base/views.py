#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

# used for http redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def home(request):
    return HttpResponseRedirect(reverse('match_list'))
