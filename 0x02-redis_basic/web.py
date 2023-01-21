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


cache = Cache()


def count_call(method: Callable) -> Callable:
    """decorator counts the number of call to a url for 10 secs"""

    @wraps(method)
    def wrapper(url):
        """counts the number of calls for the `url`"""
        result = method(url)
        cache._redis.set(url, result, 10)
        name = "count:" + url
        cache._redis.incr(name, 1)
        return result

    return wrapper


@count_call
def get_page(url: str) -> str:
    """returns the content of the `url`
    tracks the number of times a particular url was accessed
    """
    return requests.get(url).text
