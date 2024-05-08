#!/usr/bin/python3
"""list all values"""


def list_all(mongo_collection):
    """list all values"""
    if mongo_collection is not None:
        return list(mongo_collection.find())
    return []
