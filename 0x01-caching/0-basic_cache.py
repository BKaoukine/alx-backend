#!/usr/bin/python3
""" task 0 in cache module """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """basic cache class"""

    def put(self, key, item):
        """put the cache in pairs"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get the cached values"""
        return self.cache_data.get(key)
