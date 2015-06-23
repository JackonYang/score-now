#-*- coding:utf-8 -*-
import os
from django.db import models


class Match(models.Model):
    """match list

    """
    match_id = models.CharField(u'比赛 ID', max_length=32)  # col-0
    league = models.CharField(u'联赛', max_length=32)  # col-2
    home = models.CharField(u'主队', max_length=32)  # col-5
    visiting = models.CharField(u'客队', max_length=32)  # col-8
    is_betting = models.NullBooleanField(u'滚球')  # col-28
    notes = models.TextField(u'备注', max_length=500, blank=True)  # col-30
    match_date = models.DateField(auto_now=True)
    match_time = models.TimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s(%s.vs.%s)' % (self.match_id, self.home, self.visiting)


class D_Asian(models.Model):
    match_id = models.CharField(u'比赛 ID', max_length=32)
    company = models.CharField(u'足彩公司', max_length=32)  # col-0

    start_home = models.CharField(u'初盘-主队', max_length=8)  # col-2
    start_handicap = models.CharField(u'初盘-盘口', max_length=8)  # col-3
    start_visiting = models.CharField(u'初盘-客队', max_length=8)  # col-4

    real_home = models.CharField(u'即时-主队', max_length=8)  # col-5
    real_handicap = models.CharField(u'即时-盘口', max_length=8)  # col-6
    real_visiting = models.CharField(u'即时-客队', max_length=8)  # col-7

    end_home = models.CharField(u'终盘-主队', max_length=8)  # col-8
    end_handicap = models.CharField(u'终盘-盘口', max_length=8)  # col-9
    end_visiting = models.CharField(u'终盘-客队', max_length=8)  # col-10

    timestamp = models.TimeField(auto_now=True)

    def __unicode__(self):
        return '%s(Asian-%s)' % (self.match_id, self.company)
