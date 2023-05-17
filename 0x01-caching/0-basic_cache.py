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
        if (not key or not item):
            pass
        self.cache_data.update({key: item})

    def get(self, key):
        """
        return data associated with key
        """
        if (not key or key not in self.cache_data.keys()):
            return None
        return self.cache_data.get(key)
