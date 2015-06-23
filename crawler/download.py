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


# match list
url_bfdata = 'http://live.win007.com/vbsxml/bfdata.js?%s'  # timestamp
# 欧盘
url_Europe = 'http://1x2.nowscore.com/%s.js'  # match_id
# 亚盘
url_asian = 'http://vip.win007.com/AsianOdds_n.aspx?id=%s'  # match_id
url_overdown = 'http://vip.win007.com/OverDown_n.aspx?id=%s'  # match_id


def url_timestamp():
    return int(time.time()) * 1000


def req(url, encode='gbk', method='GET'):
    h = Http(timeout=2)
    headers = headers_templates.copy()
    try:
        rsp, content = h.request(url, method, headers=headers)
    except socket.timeout:
        return None
    if rsp['status'] != '404':
        return content.decode(encode).encode('utf8')


fixed_info = (  # match list, bf_data cols
        ("match_id", 0),
        ("league", 2),  # name of league
        ("home", 5),  # name of home team
        ("visiting", 8),  # name of visiting team
        ("match_time", 11),  # match start time
        ("is_betting", 28),
        ("notes", 30),
        )


# match list
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


# 欧赔只关注 4 家公司数据
# bet 365 bet 365(英国)
# Redbet Redbet(马耳他)
# Crown SB(Crown)
# Macauslot 澳门
europe_companys = {'Bet 365', 'Redbet', 'Crown', 'Macauslot'}


# 欧赔 赔率历史记录与变化时间
def europe(match_id):
    url = url_Europe % match_id
    data = req(url, 'utf8')

    if data is None:
        print 'time out'
        return

    idx_start = data.find('game=Array')  # brief info
    idx_pause = data.find('var gameDetail')  # var gameDetail line

    match_brief = data[idx_start: idx_pause]  # company id
    match_detail = data[idx_pause:]  # history data of a company

    brief_ptn = re.compile(r'"(.+?)"')
    ptn = re.compile(r'"(?:(\d+)\^(.+?))"')

    companys = {info[1]: info[2] for info in [m.split('|') for m in brief_ptn.findall(match_brief)] if info[2] in europe_companys}

    return {companys[company_id]: [item.split('|') for item in history.split(';') if item] for company_id, history in ptn.findall(match_detail) if company_id in companys.keys()}


if __name__ == '__main__':

    line = lambda t: '%s%s%s' % ('-'*20, t, '-'*20)

    print line('Match List')
    data_total = get_match_list()

    #for item in data_total:
    #    print '--'.join(item.values())

    id = data_total[0]['match_id']


    print line('Europe %s' % id)
    europe_data = europe(id)
    for company_id, history in europe_data.items():
        print company_id, history

    #print line('Asian')
    #print asian(id)[0]

    #print line('Soccer Size')
    #print soccer_size(id)[0]
