#!/usr/bin/env python3
"""Find things"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Find things"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    length = len(list(logs_collection.find()))
    arr = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{0} logs".format(length))
    print("Methods:")
    for method in arr:
        lengths = len(list(logs_collection.find({"method": method})))
        print("\tmethod {0}: {1}".format(method, lengths))

    status = len(list(logs_collection.find({"method": "GET",
                                            "path": "/status"})))
    print("{0} status check".format(status))
