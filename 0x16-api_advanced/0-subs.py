#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/N0_0ONE)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raises HTTPError for bad responses

        if response.status_code == 404:
            return 0

        data = response.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers
    except Exception as e:
        return 0

