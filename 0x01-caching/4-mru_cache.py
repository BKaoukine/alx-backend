#!/usr/bin/python3
"""LRUCache module."""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache defines a caching system with MRU eviction policy."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key: The key under which the item will be stored.
            item: The item to be stored in the cache.
        """
        if key is not None and item is not None:
            # If key already exists, remove it to update its position
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            # If cache exceeds the limit, remove the most recently used item
            if len(self.cache_data) > self.MAX_ITEMS:
                recent_key = next(reversed(self.cache_data))
                print(f"DISCARD: {recent_key}")
                self.cache_data.popitem(last=True)

    def get(self, key):
        """
        Get an item from the cache by key.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The cached item, or None if the key is not in the cache.
        """
        if key is not None and key in self.cache_data:
            item = self.cache_data.pop(key)
            # Move key to the end to mark it as most recently used
            self.cache_data[key] = item
            return item
        return None
