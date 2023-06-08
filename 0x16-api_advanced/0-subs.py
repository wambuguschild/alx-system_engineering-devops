#!/usr/bin/python3

""" A model working with Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns the number
    of subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
