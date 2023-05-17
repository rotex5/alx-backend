#!/usr/bin/python3
"""
LIFO Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Cache implememtation based on LIFO algorithm
    """

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.used_keys = []

    def put(self, key, item):
        """
        Insert data into cache
        """
        if key and item:
            cache_len = len(self.cache_data)
            if cache_len >= super().MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.used_keys[-1]))
                self.cache_data.pop(self.used_keys[-1])
                del self.used_keys[-1]
            if key in self.used_keys:
                del self.used_keys[self.used_keys.index(key)]
            self.used_keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        return corresponding value
        """
        return self.cache_data.get(key)
