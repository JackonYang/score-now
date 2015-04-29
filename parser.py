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
    ptn = re.compile(r'A\[\d+\]="(.*?)"\.split')
    return [item.split('^') for item in ptn.findall(content)]


def parse_asian(content):
    tbl1_ptn = re.compile(r'\<tr bgcolor[^>]*\>(.*?)\<\/tr\>', re.DOTALL)
    tbl1_info = re.compile(r'\<td[^>]*\>(.*?)\<\/td\>', re.DOTALL)
    return [tbl1_info.findall(item) for item in tbl1_ptn.findall(content)]


def disp(**kwargs):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('index.html')

    out_filename = 'testdata/bfdata_index.html'
    with codecs.open(out_filename, 'w', 'utf8') as f:
        f.write(template.render(**kwargs))
    print 'success! saved in %s' % os.path.abspath(out_filename)


def col_name_A():
    col_names = ['unknown']*48

    col_names[0] = u'ID'
    #col_names[1] = u'联赛 背景色'
    col_names[2] = u'联赛 简体'
    col_names[3] = u'联赛 繁体'
    col_names[4] = u'联赛 英文'
    col_names[5] = u'主队 简体'
    col_names[6] = u'主队 繁体'
    col_names[7] = u'主队 英文'
    col_names[8] = u'客队 简体'
    col_names[9] = u'客队 繁体'
    col_names[10] = u'客队 英文'

    col_names[12] = u'比赛时间基准'
    col_names[13] = u'比赛状态'

    col_names[14] = u'主队 全场 进球'
    col_names[15] = u'客队 全场 进球'
    col_names[16] = u'主队 半场 进球'
    col_names[17] = u'客队 半场 进球'

    col_names[18] = u'主队 红牌'
    col_names[19] = u'客队 红牌'
    col_names[20] = u'主队 黄牌'
    col_names[21] = u'客队 黄牌'
    #col_names[22] = u'主队 order'  # 显示在 红黄牌之前
    #col_names[23] = u'客队 order'

    #col_names[27] = u'if =1, 显示 阵容'
    col_names[28] = u'滚球'

    col_names[30] = u'备注'
    col_names[31] = u'url 联赛'
    #col_names[41] = u'if =1, 有直播'
    #col_names[47] = u'if =1, 有情报'

    return col_names


def read_file(filename):
    with open(filename, 'r') as f:
        html = f.readlines()
    return ''.join(html)


if __name__ == '__main__':

    f_bfdata = 'testdata/bfdata_1430238984000.js'
    disp(col_names=col_name_A(), data=parse_score(read_file(f_bfdata).decode('utf8')))

    f_asian = 'testdata/asian.html'
    for i in parse_asian(read_file(f_asian).decode('utf8'))[0]:
        print i
