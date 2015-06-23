#-*- coding:utf-8 -*-
from django.contrib import admin
from matches.models import Match, D_Asian


class MatchAdmin(admin.ModelAdmin):
    list_display = (
        "match_id", "league", "home", "visiting",
        'match_date', 'match_time',
        "is_betting",
        )


class D_AsianAdmin(admin.ModelAdmin):
    list_display = (
        "match_id", "company",
        "start_home", "start_handicap", "start_visiting",
        "real_home", "real_handicap", "real_visiting",
        "end_home", "end_handicap", "end_visiting",
        "timestamp",
        )


admin.site.register(Match, MatchAdmin)
admin.site.register(D_Asian, D_AsianAdmin)
