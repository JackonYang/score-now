# -*- Encoding: utf-8 -*-
import time
import re

import socket
from httplib2 import Http


headers_templates = {
    'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.65 Safari/534.24',
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


def url_timestamp():
    return int(time.time()) * 1000


def req(url, method='GET'):
    h = Http(timeout=2)
    headers = headers_templates.copy()
    try:
        rsp, content = h.request(url, method, headers=headers)
    except socket.timeout:
        return None
    return content.decode('gbk').encode('utf8')


def bfdata():
    url = url_bfdata % url_timestamp()
    data = req(url)

    if data is None:
        print 'time out'  # log
        return

    ptn = re.compile(r'A\[\d+\]="(.*?)"\.split')
    return [item.split('^') for item in ptn.findall(data)]


def clean_data(data):
    tbl1_ptn = re.compile(r'\<tr bgcolor[^>]*\>(.*?)\<\/tr\>', re.DOTALL)
    tbl1_info = re.compile(r'\<td[^>]*\>(.*?)\<\/td\>', re.DOTALL)
    return [tbl1_info.findall(item) for item in tbl1_ptn.findall(data)]


def asian(match_id):
    url = url_asian % match_id
    data = req(url)

    if data is None:
        print 'time out'
        return

    return clean_data(data)


def soccer_size(match_id):
    url = url_overdown % match_id
    data = req(url)

    if data is None:
        print 'time out'
        return

    return clean_data(data)


if __name__ == '__main__':

    line = lambda t: '%s%s%s' % ('-'*20, t, '-'*20)

    print line('Total')
    data_total = bfdata()
    print data_total[0]

    id = data_total[0][0]


    print line('Asian')
    print asian(id)[0]

    print line('Soccer Size')
    print soccer_size(id)[0]
