#!/usr/bin/python3
"""Get the number of subs on reddit"""

import requests


def number_of_subscribers(subreddit):
    """Get the number of subs on reddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'zineddine 1.0'}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        len = data.get('data').get('subscribers')
        return len
    else:
        return 0
