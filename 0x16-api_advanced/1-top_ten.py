#!/usr/bin/python3

""" Working with the Reddit API"""

import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10
    hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "DepartureNo8863"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)
