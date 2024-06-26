#!/usr/bin/python3
"""
FIFOCache module.

This module provides a caching system that uses the FIFO
(First In, First Out) eviction policy.
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache defines a caching system with FIFO eviction policy."""

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key: The key under which the item will be stored.
            item: The item to be stored in the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                print(f"DISCARD: {first_key}")
                del self.cache_data[first_key]

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
