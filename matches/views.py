#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

import datetime
import crawler.download as downloader
from matches.models import Match


def gen_match_date():
    return datetime.date


def match_list(request):
    print 'ttt'

    # download and save into database
    querysetlist=[]
    for data in downloader.get_match_list():
        kwargs = {k: v for k, v in data.items()}
        print kwargs
        querysetlist.append(Match(**kwargs))
    Match.objects.bulk_create(querysetlist)

    content = {
            'match_list': Match.objects.all(),
            }

    return render_to_response('match-list.html', RequestContext(request, content))


def europe(request, match_id):
    content = {
            'match_id': match_id,
            'history': downloader.europe(match_id),
            }
    return render_to_response('europe-history.html', RequestContext(request, content))
