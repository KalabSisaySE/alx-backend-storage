#!/usr/bin/env python3
"""the web.py module
defines the funtion `get_page`
"""
from functools import wraps
import redis
import requests
from typing import Callable, Any


class Cache:
    """uses redis to cache data"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def get(self, key: str, fn: Callable = None) -> Any:
        """retrives value from database using `key`"""
        data = self._redis.get(key)
        if data:
            if fn:
                return fn(data)
            return data


cache = Cache()


def get_page(url: str) -> str:
    """returns the content of the `url`
    tracks the number of times a particular url was accessed
    """
    name = 'count:{' + url + '}'
    if cache._redis.get(name=name):
        cache._redis.incr(name, 1)
    else:
        cache._redis.set(name, 1, 10)
    return requests.get(url).text
