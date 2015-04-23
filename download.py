# -*- Encoding: utf-8 -*-
import time
from httplib2 import Http


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


def download(url, method='GET'):
    h = Http()
    headers = headers_templates.copy()
    rsp, content = h.request(url, method, headers=headers)

    with open('tt.html', 'w') as f:
        f.write(content)
    return content


if __name__ == '__main__':
    import sys

    #url = 'http://bf.win007.com/vbsxml/alias2.js'

    while True:
        timestamp = int(time.time()) * 1000
        url = 'http://score1.win007.com/vbsxml/ch_goalBf3.xml?%s' % timestamp
        print timestamp
        print download(url)
        time.sleep(2)
