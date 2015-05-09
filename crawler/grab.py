# -*- Encoding: utf-8 -*-
from crawler import download
from crawler.models import Total


bf_cols = (
        ("match_id", 0),
        ("League", 2),
        ("name_home", 5),
        ("name_visiting", 8),
        ("t_basepoint", 12),
        ("match_status", 13),
        ("goal_home_full", 14),
        ("goal_visiting_full", 15),
        ("goal_home_half", 16),
        ("goal_visiting_half", 17),
        ("red_home", 18),
        ("red_visiting", 19),
        ("yellow_home", 20),
        ("yellow_visiting", 21),
        ("is_betting", 28),
        ("notes", 30),
        )


def get_match_list():
    querysetlist=[]
    for data in download.bfdata():
        kwargs = {k: data[idx] for k, idx in bf_cols}
        querysetlist.append(Total(**kwargs))
    Total.objects.bulk_create(querysetlist)


if __name__ == '__main__':
    get_match_list()
