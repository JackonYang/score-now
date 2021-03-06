#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.http import JsonResponse

import datetime
import crawler.download as downloader
from matches.models import Match


def gen_match_date():
    return datetime.date.today()


def match_list(request):

    match_date = gen_match_date()

    match_list = Match.objects.filter(match_date=match_date)

    if not match_list:  # download and save into database
        querysetlist=[]
        for data in downloader.get_match_list():
            kwargs = {k: v for k, v in data.items()}
            kwargs['match_date'] = match_date
            querysetlist.append(Match(**kwargs))
        Match.objects.bulk_create(querysetlist)

        # query again
        match_list = Match.objects.filter(match_date=match_date)

    content = {
            'match_list': match_list,
            }

    return render_to_response('match-list.html', RequestContext(request, content))


def europe(request, match_id):
    return JsonResponse(downloader.europe(match_id) or dict())
