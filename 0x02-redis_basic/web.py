#!/usr/bin/python3
"""the web.py module
defines the funtion `get_page`
"""
import redis
import requests


class Cache:
    """uses redis to cache data"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def get_page(self, url: str) -> str:
        """returns the content of the `url`
        tracks the number of times a particular url was accessed
        """
        response = requests.get(url)
        if self._redis.get(name=url):
            self._redis.incr(url, 1)
        else:
            self._redis.set(url, 1, 10)

        return response.text

    def count_access(self, url):
        """returns the number of access for a particular `url`"""
        return self._redis.get(url)
