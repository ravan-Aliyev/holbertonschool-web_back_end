#!/usr/bin/env python3
"""Simple pagination"""
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Getting page
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        indexes = index_range(page, page_size)
        s, e = indexes[0], indexes[1]

        try:
            return self.dataset()[s:e]
        except IndexError:
            return []


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Find page size"""
    return (page_size * (page - 1), page_size * page)
