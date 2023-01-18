#!/usr/bin/python3
"""the `exercise.py` module
defines the class `Cache`
"""
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """stores data in redis"""

    def __init__(self) -> None:
        """sets redis.Redis to a variale and flushes the db"""
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[int, bytes, str, int, float]) -> str:
        """stores a random string in a key and returns the key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
