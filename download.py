# -*- Encoding: utf-8 -*-
import time
import re
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



url_sync = 'http://score1.win007.com/vbsxml/ch_goalBf3.xml?%s'  # timestamp


def download(url, method='GET'):
    h = Http()
    headers = headers_templates.copy()
    rsp, content = h.request(url, method, headers=headers)

    with open('tt.html', 'w') as f:
        f.write(content)
    return content

def keep_alive(func, interval=2):
    while True:
        timestamp = int(time.time()) * 1000
        url = url_sync % timestamp
        data = download(url)
        # test data
        # data = r"<?xml  version='1.0' encoding='UTF-8'?><c><match><m>1123193,4627486,0,0.90,1.00,47188050,1.03,10.00,75.00,4156215,3.50,3.70,0.16,1,1,1,1</m></match></c>"

        print data

        new_match = re.compile(r'<m>(.*?)</m>')
        func(new_match.findall(data), timestamp)

        time.sleep(interval)



if __name__ == '__main__':
    import sys

    def out(seq, timestamp):
        print '%s%d%s' % ('-' * 20, timestamp, '-'*20)
        print seq

    keep_alive(out)
