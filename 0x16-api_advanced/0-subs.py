#!/usr/bin/python3
"""This module have a function that quaries the Reddit API
and returns number of subscribers for a given subreddit"""


from requests import get


def number_of_subscribers(subreddit):
    """Return number of subscribers including not active users
    or zero at not valid subreddit"""

    url = "https://www.reddit.com/" + 'r/' + subreddit + '/about.json'
    myHeaders = {'User-Agent': 'Custom User-Agent'}
    res = get(url, headers=myHeaders, allow_redirects=False)

    if res.status_code == 200:
        return res.json().get('data').get('subscribers')
    else:
        return 0
