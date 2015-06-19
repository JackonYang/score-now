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


url_bfdata = 'http://live.win007.com/vbsxml/bfdata.js?%s'  # timestamp
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


fixed_info = (  # match list, bf_data cols
        ("match_id", 0),
        ("league", 2),  # name of league
        ("home", 5),  # name of home team
        ("visiting", 8),  # name of visiting team
        ("t_basepoint", 12),  # match start time basepoint
        ("is_betting", 28),
        ("notes", 30),
        )


def get_match_list():
    url = url_bfdata % url_timestamp()
    data = req(url)

    if data is None:
        print 'time out'  # raise error
        return

    ptn = re.compile(r'A\[\d+\]="(.*?)"\.split')
    m = [item.split('^') for item in ptn.findall(data)]
    return [{k: item[idx] for k, idx in fixed_info} for item in m]


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
    data_total = get_match_list()

    for item in data_total:
        print '--'.join(item.values())

    id = data_total[0][0]


    print line('Asian')
    print asian(id)[0]

    print line('Soccer Size')
    print soccer_size(id)[0]
