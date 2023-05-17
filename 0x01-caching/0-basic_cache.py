#!/usr/bin/python3
"""
Implementing a Cache using a Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Class Implementation of a Basic Cache
    """

    def put(self, key, item):
        """
        inserting data into cache dictionay
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        return data associated with key
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
