#!/usr/bin/env python3
"""
LFUCache module implementing a cache system using the
Least Frequently Used (LFU) caching algorithm with an LRU fallback.
"""

from base_caching import BaseCaching
import time


class LFUCache(BaseCaching):
    """
    LFUCache is a caching system with LFU policy,
    evicting the least frequently used items first.
    When frequencies match, it uses the LRU (Least Recently Used) strategy.
    """

    def __init__(self):
        """
        Initialize the LFUCache with cache, frequency tracking, and LRU tracking.
        """
        super().__init__()
        self.usage_frequency = {}  # Dictionary to track the frequency of each key
        self.recently_used = {}    # Dictionary to track last access time for each key

    def put(self, key, item):
        """
        Adds an item to the cache using LFU + LRU policies.

        If the cache exceeds BaseCaching.MAX_ITEMS, it removes
        the least frequently used item. If multiple items have the same
        frequency, it uses the least recently used (LRU) policy to break ties.

        Args:
            key (str): The key for the item.
            item (Any): The item to cache.
        """
        if key is None or item is None:
            return

        # Add or update the cache data
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find least frequently used items
                min_freq = min(self.usage_frequency.values())
                least_used = [k for k, freq in self.usage_frequency.items() if freq == min_freq]

                # Apply LRU on least frequently used items if needed
                if len(least_used) > 1:
                    lru_item = min(least_used, key=lambda k: self.recently_used[k])
                    self._discard(lru_item)
                else:
                    self._discard(least_used[0])

            # Add the new item to the cache
            self.cache_data[key] = item
            self.usage_frequency[key] = 1

        # Update the access order
        self.recently_used[key] = time.time()

    def get(self, key):
        """
        Retrieves an item from the cache.

        Updates both frequency and access time for the item if found.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            Any: The cached item, or None if not found.
        """
        if key is None or key not in self.cache_data:
            return None

        # Increase access frequency and update access time
        self.usage_frequency[key] += 1
        self.recently_used[key] = time.time()
        return self.cache_data[key]

    def _discard(self, key):
        """
        Removes an item from the cache, updating necessary tracking structures.

        Args:
            key (str): The key of the item to discard.
        """
        del self.cache_data[key]
        del self.usage_frequency[key]
        del self.recently_used[key]
        print(f"DISCARD: {key}")
