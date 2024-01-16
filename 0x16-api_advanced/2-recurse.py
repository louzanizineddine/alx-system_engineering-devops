#!/usr/bin/python3
"""ecursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    hdrs = {
        "User-Agent": "Mozilla/5"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res = requests.get(url, headers=hdrs, params=params, allow_redirects=False)
    if res.status_code == 404:
        return None

    result = res.json().get("data")
    after = result.get("after")
    count += result.get("dist")
    for c in result.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
