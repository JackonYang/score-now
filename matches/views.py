#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response


from crawler.download import get_match_list

def match_list(request):

    content = {
            'match-list': get_match_list(),
            }

    return render_to_response('match-list.html', RequestContext(request, content))
