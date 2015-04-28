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



url_init = 'http://score.win007.com/vbsxml/goalBf3.xml?%s'  # timestamp
url_sync = 'http://score.win007.com/vbsxml/ch_goalBf3.xml?%s'  # timestamp
url_bfdata = 'http://score.win007.com/vbsxml/bfdata.js?%s'  # timestamp


def req(url, method='GET'):
    h = Http(timeout=2)
    headers = headers_templates.copy()
    try:
        rsp, content = h.request(url, method, headers=headers)
    except socket.timeout:
        return None
    return content

def keep_alive(func, interval=2):
    while True:
        start_time = time.time()
        timestamp = int(start_time) * 1000
        url = url_sync % timestamp
        data = req(url)
        # test data
        # data = r"<?xml  version='1.0' encoding='UTF-8'?><c><match><m>1123193,4627486,0,0.90,1.00,47188050,1.03,10.00,75.00,4156215,3.50,3.70,0.16,1,1,1,1</m></match></c>"

        if data is not None:
            new_match = re.compile(r'<m>(.*?)</m>')
            func(new_match.findall(data), timestamp)
        else:
            print 'time out'

        time.sleep(interval)

def init_score(func):
    timestamp = url_timestamp()
    data = req(url_init % timestamp)

    if data is not None:
        new_match = re.compile(r'<m>(.*?)</m>')
        init_data = [item.split(',') for item in new_match.findall(data)]
        for m in init_data:
            print m
    else:
        print 'time out'  # TODO: log

def bfdata(func):
    t_req = url_timestamp()
    url = url_bfdata % url_timestamp()
    data = req(url).decode('gbk').encode('utf8')

    if data is None:
        print 'time out'
        return

    return func(data, t_req, 'bfdata')



if __name__ == '__main__':
    import sys

    def out(seq, timestamp):
        print '%s%d%s' % ('-' * 20, timestamp, '-'*20)
        print seq

    def out_file(content, request_time, identifier):
        with open('testdata/%s_%s.js' % (identifier, request_time), 'w') as f:
            f.write(content or 'error')

    bfdata(out_file)
