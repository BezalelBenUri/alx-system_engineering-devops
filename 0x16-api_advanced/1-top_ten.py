#!/usr/bin/python3
""" module for function to return top 10 hot posts of a given subreddit """
import requests
import sys


def top_ten(subreddit):
    """ Returns: top ten post titles
        or None if queried subreddit is invalid """
    headers = {'User-Agent': 'PhenomenalAI'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        post_titles = response.json().get('data').get('children')
        for post_title in post_titles:
            print(post_title.get('data').get('title'))
    else:
        print(None)
