# -*- Encoding: utf-8 -*-
import time
import re

import socket
from httplib2 import Http

from util import url_timestamp


headers_templates = { 'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.65 Safari/534.24',
    'Content-type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Accept-Charset': 'UTF-8,*;q=0.5',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'Referer': 'http://score1.win007.com/',
    'Connection': 'keep-alive',
}



url_bfdata = 'http://score.win007.com/vbsxml/bfdata.js?%s'  # timestamp
url_asian = 'http://vip.win007.com/AsianOdds_n.aspx?id=%s'  # match_id
url_overdown = 'http://vip.win007.com/OverDown_n.aspx?id=%s'  # match_id


def req(url, method='GET'):
    h = Http(timeout=2)
    headers = headers_templates.copy()
    try:
        rsp, content = h.request(url, method, headers=headers)
    except socket.timeout:
        return None
    return content


def bfdata(func):
    t_req = url_timestamp()
    url = url_bfdata % url_timestamp()
    data = req(url).decode('gbk').encode('utf8')

    if data is None:
        print 'time out'
        return

    return func(data, 'testdata/bfdata_%s.js' % t_req)


def asian(match_id, func):
    url = url_asian % match_id
    data = req(url).decode('gbk').encode('utf8')

    if data is None:
        print 'time out'
        return
    return func(data, 'testdata/asian.html')


def SoccerSize(match_id, func):
    url = url_overdown % match_id
    data = req(url).decode('gbk').encode('utf8')

    if data is None:
        print 'time out'
        return
    return func(data, 'testdata/SoccerSize.html')


if __name__ == '__main__':
    import sys

    def out_file(content, filename):
        with open(filename, 'w') as f:
            f.write(content or 'error')


    #bfdata(out_file)
    #asian('1081262', out_file)
    SoccerSize('1096621', out_file)
