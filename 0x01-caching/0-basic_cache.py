#!/usr/bin/python3
"""
BasicCache module.

This module provides a basic caching system implementation.
"""

BaseCaching = __import__('BaseCaching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache defines a simple caching system."""

    def __init__(self):
        """Initialize the cache."""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key: The key under which the item will be stored.
            item: The item to be stored in the cache.
        """
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache by key.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The cached item, or None if the key is not in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
