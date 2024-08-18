#!/usr/bin/env python3
"""
Cache Class Module
"""
import uuid
import redis
from typing import Union


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Function to store data
        """
        r_key = str(uuid.uuid4())
        self._redis.set(r_key, data)
        return r_key
