# -*- coding: utf-8 -*-
import pandas as pd
import neurokit2 as nk
import json
import urllib.request


def github_contributors(repo="user/repo", access_token="access_token"):
    """Access the contributors list from GitHub

    You need your access token that you can get by following these instructions:
    https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line

    Examples
    ---------
    >>> import popularipy
    >>> data = popularipy.github_contributors("neuropsychology/neurokit", "myaccesstoken")
    >>> print("Number of contributors" + str(len(data)))
    """
    page_number = 0
    contributors_remaining = True

    contributor = []
    contributions = []
    while contributors_remaining:
        query_url = "https://api.github.com/repos/%s/contributors?page=%s&access_token=%s" % (repo, page_number, access_token)

        req = urllib.request.Request(query_url)
        req.add_header('Accept', 'application/vnd.github.v3.star+json')
        try:
            response = urllib.request.urlopen(req)
        except:
            pass
        data = json.loads(response.read())

        for user in data:
            contributor.append(user["login"])
            contributions.append(user["contributions"])

        if len(data) < 25:
            contributors_remaining = False

        page_number += 1


    data = pd.DataFrame({"Contributor": contributor,
                         "Contributions": contributions})
    
    data = data.drop_duplicates()

    return data
