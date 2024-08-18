#!/usr/bin/env python3
"""
Cache Class Module
"""
import uuid
import redis
from typing import Union, Callable

def count_calls(method: Callable) -> Callable:
    """ # of calls made to Cashe class methods
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """returns the method after incrementing call counter
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

    return wrapper

class Cache():
    """
    Cache class
    """
    def __init__(self):
        """
        The init method
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def get(self, key: str, fn: Callable = None) -> Union[
            str, bytes, int, float]:
        """
        get method
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Function to store data
        """
        r_key = str(uuid.uuid4())
        self._redis.set(r_key, data)
        return r_key

    def get_str(self, key: str) -> str:
        """
        get from str
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """get from int
        """
        return self.get(key, lambda x: int(x))
