#!/usr/bin/env python3
"""Web cache and tracker.
"""
from functools import wraps
from typing import Callable

import redis
import requests

redis_store = redis.Redis()
"""Global Redis store.
"""


def data_cacher(method: Callable) -> Callable:
    """Decorator to cache the output of a method.
    """

    @wraps(method)
    def invoker(url) -> str:
        """Invoke the method and cache the result.
        """
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result

    return invoker


@data_cacher
def get_page(url: str) -> str:
    """Get the content of a web page.
    """
    return requests.get(url).text
