#!/usr/bin/env python3
"""
LRU Caching Implementation
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Cache implememtation based on LRU algorithm
    """

    def __init__(self):
        super().__init__()
        self.used_keys = []

    def put(self, key, item):
        """
        Insert data into cache
        """
        if key and item:
            # Check if key already exists in the cache
            if key in self.cache_data:
                # Remove key from the order
                self.used_keys.remove(key)
            elif len(self.cache_data) >= super().MAX_ITEMS:
                # Remove the least recently used key
                lru_key = self.used_keys.pop(0)
                print("DISCARD: {}".format(lru_key))
                del self.cache_data[lru_key]

            # Add key to the end of the order
            self.used_keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        return corresponding value
        """
        if key is None or key not in self.cache_data:
            return None

        self.used_keys.remove(key)  # Remove key from the used_keys
        self.used_keys.append(key)  # Add key to the end of the used_keys

        return self.cache_data.get(key)
