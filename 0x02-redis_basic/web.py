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


cache = Cache()


def get_page(url: str) -> str:
    """returns the content of the `url`
    tracks the number of times a particular url was accessed
    """
    cache._redis.set(url, requests.get(url).text, 10)
    name = "count:{}".format(url)
    cache._redis.incr(name, 1)
