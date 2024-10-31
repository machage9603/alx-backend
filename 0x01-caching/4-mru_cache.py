#!/usr/bin/env python3
""" BasicCache module """

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRUCache defines an MRU caching system"""
    def __init__(self):
        """Initializes variable"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """Gets an item by key"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
