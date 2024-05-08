#!/usr/bin/python3
"""list all values"""


def insert_school(mongo_collection, **kwargs):
    """list all values"""
    return mongo_collection.insert_one(kwargs)
