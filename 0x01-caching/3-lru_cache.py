#!/usr/bin/python3
"""
LRUCache module.

This module provides a caching system that uses the LRU
(Least Recently Used) eviction policy.
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache defines a caching system with LRU eviction policy."""

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
            # Add key to the end to mark it as recently used
            self.cache_data[key] = item
            # If the cache exceeds the maximum size
            # remove the first item (least recently used)
            if len(self.cache_data) > self.MAX_ITEMS:
                oldest_key = next(iter(self.cache_data))
                print(f"DISCARD: {oldest_key}")
                self.cache_data.popitem(last=False)

    def get(self, key):
        """
        Get an item from the cache by key.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The cached item, or None if the key is not in the cache.
        """
        item = self.cache_data.get(key)
        if item is not None:
            # Move the accessed item to the end to mark it as recently used
            self.cache_data.move_to_end(key)
        return item
