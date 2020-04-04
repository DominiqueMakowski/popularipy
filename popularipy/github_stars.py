# -*- coding: utf-8 -*-
import pandas as pd
import neurokit2 as nk
import json
import urllib.request
import datetime


def github_stars(repo="user/repo", access_token="access_token"):
    """Access the stars history from GitHub

    You need your access token that you can get by following these instructions:
    https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line

    Examples
    ---------
    >>> import popularipy
    >>> data = popularipy.github_stars("neuropsychology/neurokit", "myaccesstoken")
    >>> data.plot(x="Date")
    """
    page_number = 0
    stars_remaining = True
    stars_times = []
    stars_users = []
    while stars_remaining:
        query_url = "https://api.github.com/repos/%s/stargazers?page=%s&access_token=%s" % (repo, page_number, access_token)

        req = urllib.request.Request(query_url)
        req.add_header('Accept', 'application/vnd.github.v3.star+json')
        try:
            response = urllib.request.urlopen(req)
        except:
            pass
        data = json.loads(response.read())

        for user in data:
            username = user['user']['login']

            star_time = datetime.datetime.strptime(user['starred_at'],'%Y-%m-%dT%H:%M:%SZ')
            star_time = star_time + datetime.timedelta(hours=-5) # EST
            star_time = star_time.strftime('%Y-%m-%d %H:%M:%S')
            stars_times.append(star_time)

            stars_users.append(username)


        if len(data) < 25:
            stars_remaining = False

        page_number += 1


    data = pd.DataFrame({"Date": stars_times,
                         "User": stars_users})
    data = data.drop_duplicates(subset ="User")
    data["Stars"] = 1
    data["Stars"] = data["Stars"].cumsum()
    data = data.append({'Date' : datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') ,
                        'User' : "MrBrownstone",
                        "Stars": data["Stars"].values[-1]} , ignore_index=True)
    data = data.drop_duplicates(subset ="Date")
    data.index = pd.DatetimeIndex(data["Date"])

    data = data.resample('D').fillna("backfill")
    data = data.drop(["Date", "User"], axis=1)
    data = data.reset_index()
    data["Date"] = pd.to_datetime(data["Date"]).dt.strftime('%d %b %Y')

    return data
