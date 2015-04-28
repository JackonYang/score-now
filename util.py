# -*- Encoding: utf-8 -*-
import time

def url_timestamp():
    return int(time.time()) * 1000


if __name__ == '__main__':
    print url_timestamp()
