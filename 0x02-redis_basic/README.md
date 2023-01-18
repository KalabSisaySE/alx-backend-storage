# 0x02. Redis basic

## [TASK-0](./exercise.py)

***Writing strings to Redis***

Create a `Cache` class. In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using `flushdb`.

Create a `store` method that takes a `data` argument and returns a string. The method should generate a random key (e.g. using `uuid`), store the input data in Redis using the random key and return the key.

Type-annotate `store` correctly. Remember that `data` can be a `str`, `bytes`, `int` or `float`.

``` shell
bob@dylan:~$ cat main.py
```

``` python
#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
```

``` shell
bob@dylan:~$ python3 main.py 
3a3e8231-b2f6-450d-8b0e-0f38f16e8ca2
b'hello'
bob@dylan:~$ 
```

## [TASK-5](./web.py)

***Implementing an expiring web cache and tracker***

In this tasks, we will implement a `get_page` function (prototype: `def get_page(url: str) -> str:`). The core of the function is very simple. It uses the `requests` module to obtain the HTML content of a particular URL and returns it.

Start in a new file named `web.py` and do not reuse the code written in `exercise.py`.

Inside `get_page` track how many times a particular URL was accessed in the key "count:{url}" and cache the result with an expiration time of 10 seconds.

Tip: Use `http://slowwly.robertomurray.co.uk` to simulate a slow response and test your caching.

Bonus: implement this use case with decorators.

### Links

- [Redis commands](https://redis.io/commands/)
- [Redis python client](https://redis-py.readthedocs.io/en/stable/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)
- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)
