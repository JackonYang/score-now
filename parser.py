# -*- Encoding: utf-8 -*-
import os
import re
import json
import codecs
import time
import sys

from httplib2 import Http
from jinja2 import Environment, FileSystemLoader


template_dir = "templates"


def parse_score(content):
    #ptn = re.compile(r'A\[(\d+)\]="(.*?)".split\(\'^\'\);')
    ptn = re.compile(r'A\[\d+\]="(.*?)"\.split')
    return [item.split('^') for item in ptn.findall(content)]


def disp(**kwargs):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('index.html')

    out_filename = 'testdata/bfdata_index.html'
    with codecs.open(out_filename, 'w', 'utf8') as f:
        f.write(template.render(**kwargs))
    print 'success! saved in %s' % os.path.abspath(out_filename)


if __name__ == '__main__':
    filename = 'testdata/bfdata_1430238984000.js'
    with open(filename, 'r') as f:
        html = f.readlines()

    col_names = ['unknown']*48

    col_names[5] = u'主队 简体'
    col_names[6] = u'主队 繁体'
    col_names[7] = u'主队 英文'
    col_names[8] = u'客队 简体'
    col_names[9] = u'客队 繁体'
    col_names[10] = u'客队 英文'

    disp(col_names=col_names, data=parse_score(''.join(html).decode('utf8')))
