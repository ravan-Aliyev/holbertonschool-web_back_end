#!/usr/bin/env python3
"""list all values"""


def update_topics(mongo_collection, name, topics):
    """list all values"""
    myquery = {"name": name}
    newvalues = {"$set": {"topics": topics}}
    return mongo_collection.update_many(myquery, newvalues)
