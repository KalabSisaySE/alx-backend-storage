#!/usr/bin/env python3
"""the `exercise.py` module
defines the class `Cache`
"""
import redis
from typing import Union, Callable, Any
from uuid import uuid4


class Cache:
    """stores data in redis"""

    def __init__(self) -> None:
        """sets redis.Redis to a variale and flushes the db"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores `data` (value) in a random string key and returns the key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Any:
        """retrives value from database using `key`"""
        data = self._redis.get(key)
        if data:
            if fn:
                return fn(data)
            return data

    def get_str(self, byte):
        """returns utf-8 decoded string from `byte`"""
        return byte.decode("utf-8")

    def get_int(self, byte):
        """returns int conversion of `byte`"""
        return int(byte)
