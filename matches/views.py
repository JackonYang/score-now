#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response


import crawler.download as downloader

def match_list(request):

    content = {
            'match_list': downloader.get_match_list(),
            }

    return render_to_response('match-list.html', RequestContext(request, content))

def europe(request, match_id):
    content = {
            'match_id': match_id,
            'history': downloader.europe(match_id),
            }
    return render_to_response('europe-history.html', RequestContext(request, content))
