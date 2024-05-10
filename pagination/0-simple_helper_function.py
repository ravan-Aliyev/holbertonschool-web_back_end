#!/usr/bin/env python3
"""Find page size"""


def index_range(page, page_size):
    """Find page size"""
    return (page_size * (page - 1), page_size * page)