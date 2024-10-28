#!/usr/bin/env python3
import sys, os
"""
Main file
"""
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
Server = __import__('2-hypermedia_pagination').Server

server = Server()

print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))
