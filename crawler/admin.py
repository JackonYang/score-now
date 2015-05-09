#-*- coding:utf-8 -*-
from django.contrib import admin
from crawler.models import Total, D_Asian


class TotalAdmin(admin.ModelAdmin):
    list_display = (
        "match_id", "League",
        "name_home", "name_visiting",
        "t_basepoint", "match_status",
        "goal_home_full", "goal_visiting_full",
        "goal_home_half", "goal_visiting_half",
        "red_home", "red_visiting",
        "yellow_home", "yellow_visiting",
        "is_betting", "notes", 'timestamp')


class D_AsianAdmin(admin.ModelAdmin):
    list_display = (
        "match_id", "company",
        "start_home", "start_handicap", "start_visiting",
        "real_home", "real_handicap", "real_visiting",
        "end_home", "end_handicap", "end_visiting",
        "timestamp",
        )


admin.site.register(Total, TotalAdmin)
admin.site.register(D_Asian, D_AsianAdmin)
