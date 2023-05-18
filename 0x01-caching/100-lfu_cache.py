from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    Cache implememtation based on LFU algorithm
    """
    def __init__(self):
        """
        Insert data into cache
        """
        super().__init__()
        self.frequency = defaultdict(int)

    def put(self, key, item):
        """
        Insert data into cache
        """
        if key and item:
            # Check if the key already exists in the cache
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                # If the cache is full, discard the least frequency used item
                if len(self.cache_data) >= super().MAX_ITEMS:
                    self.discard_least_frequent()

                self.cache_data[key] = item
                self.frequency[key] = 1

    def get(self, key):
        """
        return corresponding value
        """
        if key is None or key not in self.cache_data:
            return None
        # Increment the frequency count for the key
        self.frequency[key] += 1
        return self.cache_data.get(key)

    def discard_least_frequent(self):
        """
        selects the least frequent key for eviction
        based on the frequency values
        """
        # Find the minimum frequency in the cache
        min_freq = min(self.frequency.values())

        # Find the keys with the minimum frequency
        min_freq_keys = [k for k, v in self.frequency.items() if v == min_freq]

        if len(min_freq_keys) == 1:
            # If only one key has the minimum frequency, discard it
            key_to_discard = min_freq_keys[0]
        else:
            # If multiple keys have the same minimum frequency,
            # use LRU to break the tie
            lru_key = min_freq_keys[0]
            for key in min_freq_keys:
                if self.frequency[key] < self.frequency[lru_key]:
                    lru_key = key
            key_to_discard = lru_key

        # Discard the least frequency used key
        del self.cache_data[key_to_discard]
        del self.frequency[key_to_discard]

        print("DISCARD: {}".format(key_to_discard))
