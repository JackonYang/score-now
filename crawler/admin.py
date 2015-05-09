#-*- coding:utf-8 -*-
from django.contrib import admin
from crawler.models import Total, D_Asian


class TotalAdmin(admin.ModelAdmin):
    list_display = (
        "match_id",
        "name_home",
        "t_basepoint",
        "goal_home_full",
        "goal_home_half",
        "red_home",
        "yellow_home",
        "is_betting", "notes", 'timestamp')


class D_AsianAdmin(admin.ModelAdmin):
    list_display = (
        "match_id", "company",
        "start_home", "start_handicap", "start_visiting",
        "real_home", "real_handicap", "real_visiting",
        "end_home", "end_handicap", "end_visiting"
        )


admin.site.register(Total, TotalAdmin)
admin.site.register(D_Asian, D_AsianAdmin)
