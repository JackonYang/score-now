# -*- Encoding: utf-8 -*-
from crawler import download
from crawler.models import Total, D_Asian


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

detail_cols = (
        ("company", 0),
        ("start_home", 2),
        ("start_handicap", 3),
        ("start_visiting", 4),
        ("real_home", 5),
        ("real_handicap", 6),
        ("real_visiting", 7),
        ("end_home", 8),
        ("end_handicap", 9),
        ("end_visiting", 10),
        )




def get_match_list():
    querysetlist=[]
    for data in download.bfdata():
        kwargs = {k: data[idx] for k, idx in bf_cols}
        querysetlist.append(Total(**kwargs))
    Total.objects.bulk_create(querysetlist)


def get_match_asian(match_id):
    querysetlist=[]
    for data in download.asian(match_id):
        kwargs = {k: data[idx] for k, idx in detail_cols}
        querysetlist.append(D_Asian(match_id=match_id, **kwargs))
    D_Asian.objects.bulk_create(querysetlist)


if __name__ == '__main__':
    get_match_list()

    i = 0
    for match in Total.objects.all():
        try:
            get_match_asian(match.match_id)
        except:
            print 'error! match ID: %s' %  match.match_id
        else:
            i += 1
            print i
