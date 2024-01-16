#!/usr/bin/python3
"""Query the reddit api"""
import requests


def recurse(subreddit, hot_list=[]):
    """Query the reddit api"""
    try:
        listing = 'top'
        limit = 10
        timefrm = 'all'
        headers = {'User-agent': 'Mozilla/5'}
        redit = 'https://www.reddit.com/r/'
        sub = subreddit
        url_req = f'{redit}{sub}/{listing}.json?limit={limit}&t={timefrm}'

        res = requests.get(url_req, headers=headers)

        if res.status_code == 200:
            data = res.json()
            top = data['data']['children']
            for post in data['data']['children']:
                x = post['data']['title']
                hot_list.append(x)
            return (hot_list)
        else:
            return (None)
    except Exception:
        return (0)
