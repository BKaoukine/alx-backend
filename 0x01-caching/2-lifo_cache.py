#!/usr/bin/python3
"""
LIFOCache module.

This module provides a caching system that uses the LIFO
(Last In, First Out) eviction policy.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines a caching system with LIFO eviction policy."""

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key: The key under which the item will be stored.
            item: The item to be stored in the cache.
        """
        len_cach_data = len(self.cache_data)

        if key is not None and item is not None:
            if len_cach_data >= self.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[len_cach_data-1]
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]

            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache by key.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The cached item, or None if the key is not in the cache.
        """
        return self.cache_data.get(key)
