#!/usr/bin/env python3
""" Module to create a simple cache.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Class to implement basic cache.
        - It inherits from BaseCaching
    """
    def put(self, key, item):
        """ Add an item to cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from cache by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
