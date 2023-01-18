#!/usr/bin/python3
"""the web.py module
defines the funtion `get_page`
"""
import redis
import requests


def get_page(self, url: str) -> str:
    """returns the content of the `url`
    tracks the number of times a particular url was accessed
    """
    response = requests.get(url)
    if redis.Redis.get(name=url):
        redis.Redis.incr(url, 1)
    else:
        redis.Redis.set(url, 1, 10)

    return response.text
