#!/usr/bin/python3
"""get the top 10 posts on a given subreddit"""

import requests


def top_ten(subreddit):
    """get the top 10 posts on a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
    try:
        res = requests.get(url, headers=headers,
                                allow_redirects=False)
        if res.status_code == 200:
            titles = res.json().get('data').get('children')
            for i in range(10):
                print(titles[i].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
