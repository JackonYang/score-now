#-*- coding:utf-8 -*-
import os
from django.db import models


class Total(models.Model):
    """match list data model

    """
    match_id = models.CharField(u'比赛 ID', max_length=32)  # col-0
    League = models.CharField(u'联赛', max_length=32)  # col-2
    name_home = models.CharField(u'主队', max_length=32)  # col-5
    name_visiting = models.CharField(u'客队', max_length=32)  # col-8
    t_basepoint = models.CharField(u'比赛时间基准', max_length=32)  # col-12
    match_status = models.CharField(u'比赛状态', max_length=2)  # col-13
    goal_home_full = models.CharField(u'进球-主队-全场', max_length=4)  # col-14
    goal_visiting_full = models.CharField(u'进球-客队-全场', max_length=4)  # col-15
    goal_home_half = models.CharField(u'进球-主队-半场', max_length=4)  # col-16
    goal_visiting_half = models.CharField(u'进球-客队-半场', max_length=4)  # col-17
    red_home = models.CharField(u'红牌-主队', max_length=4)  # col-18
    red_visiting = models.CharField(u'红牌-客队', max_length=4)  # col-19
    yellow_home = models.CharField(u'黄牌-主队', max_length=4)  # col-20
    yellow_visiting = models.CharField(u'黄牌-客队', max_length=4)  # col-21
    is_betting = models.NullBooleanField(u'滚球')  # col-28
    notes = models.TextField(u'备注', max_length=500, blank=True)  # col-30
    timestamp = models.TimeField(auto_now=True)

    def __unicode__(self):
        return '%s(%s.vs.%s)' % (self.match_id, self.name_home, self.name_visiting)
