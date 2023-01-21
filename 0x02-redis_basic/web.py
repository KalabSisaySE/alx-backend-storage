#!/usr/bin/python3
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


def count_call(method: Callable) -> Callable:
    """decorator counts the number of call to a url for 10 secs"""

    @wraps(method)
    def wrapper(url):
        """counts the number of calls for the `url`"""
        name = "count:{}".format(url)
        if cache._redis.get(name=name):
            cache._redis.incr(name, 1)
        else:
            cache._redis.set(name, 1, 10)
        return method(url)

    return wrapper


@count_call
def get_page(url: str) -> str:
    """returns the content of the `url`
    tracks the number of times a particular url was accessed
    """
    response = requests.get(url)
    return response.text
