#!/usr/bin/env python3
"""the `exercise.py` module
defines the class `Cache`
"""
import redis
from functools import wraps
from typing import Union, Callable, Any
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """a decorator that will count the number of times a method is called"""

    @wraps(method)
    def wrapper(self, *args):
        """increments the key(function name) everytime it is called"""
        name = method.__qualname__
        self._redis.incr(name, 1)
        return method(self, *args)

    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator that saves the history of a function call"""

    @wraps(method)
    def wrapper(self, *args):
        """saves inputs and outputs on the function call in two redis lists"""
        inputs = method.__qualname__ + ":inputs"
        outputs = method.__qualname__ + ":outputs"
        self._redis.rpush(inputs, str(args))
        output = method(self, *args)
        self._redis.rpush(outputs, output)
        return output

    return wrapper


class Cache:
    """stores data in redis"""

    def __init__(self) -> None:
        """sets redis.Redis to a variale and flushes the db"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def replay(self, fn_name):
        """displays the history of calls for a particular function"""
        inputs = fn_name.__qualname__ + ":inputs"
        outputs = fn_name.__qualname__ + ":outputs"
        inp_list = self._redis.lrange(inputs, 0, -1)
        out_list = self._redis.lrange(outputs, 0, -1)

        print(
            "{} was called {} times".format(
                fn_name.__qualname__,
                len(inp_list)
            )
        )

        for inp, out in zip(inp_list, out_list):
            print(
                "{}(*{}) -> {}".format(
                    fn_name.__qualname__,
                    inp.decode("utf-8"),
                    out.decode("utf-8")
                )
            )
