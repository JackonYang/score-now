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
            'companys': {
                '48408691': u'bet 365(英国)',
                '48417881': u'Redbet(马耳他)',
                '48407436': u'SB(Crown)',
                '48424205': u'澳门',
                },
            }
    return render_to_response('europe-history.html', RequestContext(request, content))
