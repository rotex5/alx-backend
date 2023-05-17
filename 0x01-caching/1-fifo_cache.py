#!/usr/bin/python3
"""
FIFO Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Cache implememtation based on FIFO algorithm
    """
    def __init__(self):
        """Constructor"""
        super().__init__()

    def put(self, key, item):
        """
        Insert data into cache
        """
        if (key is None or item is None):
            pass

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            if (key in self.cache_data):
                self.cache_data[key] = item
            else:
                first_key = list(self.cache_data.keys())[0]
                print("DISCARD: {}".format(first_key))
                self.cache_data.pop(first_key)

        self.cache_data[key] = item

    def get(self, key):
        """
        return corresponding value
        """
        return self.cache_data.get(key, None)
