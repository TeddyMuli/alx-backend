#!/usr/bin/env python3
import sys, os
"""
Main file
"""

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)
