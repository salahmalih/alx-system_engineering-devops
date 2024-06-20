#!/usr/bin/python3
"""This module contains a function that queries the Reddit API
and returns the number of subscribers for a given subreddit."""

from requests import get


def number_of_subscribers(subreddit):
    """Return the number of subscribers (including inactive
    users) for a given subreddit,
    or zero if the subreddit is invalid."""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'}
    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json().get('data', {})
            return data.get('subscribers', 0)
        except ValueError:
            return 0
    else:
        return 0
