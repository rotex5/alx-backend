#!/usr/bin/env python3
"""
LFU Caching Implementation
"""
from collections import defaultdict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Cache implememtation based on LFU algorithm:wq
    """
    def __init__(self):
        """
        Insert data into cache
        """
        super().__init__()
        self.item_freq = defaultdict(int)

    def put(self, key, item):
        """
        Insert data into cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.item_freq[key] += 1
            else:
                if len(self.cache_data) >= super().MAX_ITEMS:
                    self.discard_least_frequent()

                self.cache_data[key] = item
                self.item_freq[key] = 1

    def get(self, key):
        """
        return corresponding value
        """
        if key is None or key not in self.cache_data:
            return None
        self.item_freq[key] += 1
        return self.cache_data.get(key)

    def discard_least_frequent(self):
        """
        selects the least frequent key for eviction
        based on the frequency values
        """
        min_freq = min(self.item_freq.values())

        min_freq_keys = [k for k, v in self.item_freq.items() if v == min_freq]

        if len(min_freq_keys) == 1:
            key_to_discard = min_freq_keys[0]
        else:
            lru_key = min_freq_keys[0]
            for key in min_freq_keys:
                if self.item_freq[key] < self.item_freq[lru_key]:
                    lru_key = key
            key_to_discard = lru_key

        del self.cache_data[key_to_discard]
        del self.item_freq[key_to_discard]

        print("DISCARD: {}".format(key_to_discard))
