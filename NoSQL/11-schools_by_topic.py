#!/usr/bin/env python3
"""list all values"""


def schools_by_topic(mongo_collection, topic):
    """list all values"""
    return mongo_collection.find({"topics": topic})
