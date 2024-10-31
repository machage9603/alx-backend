#!/usr/bin/env python3
""" BasicCache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines a LIFO caching system"""
    def __init__(self):
        """Initializes variables"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-2]
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]

    def get(self, key):
        """Gets an item by key"""
        return self.cache_data.get(key, None)
