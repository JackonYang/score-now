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

    return func(data, t_req, 'bfdata')



if __name__ == '__main__':
    import sys

    def out_file(content, request_time, identifier):
        with open('testdata/%s_%s.js' % (identifier, request_time), 'w') as f:
            f.write(content or 'error')


    bfdata(out_file)
