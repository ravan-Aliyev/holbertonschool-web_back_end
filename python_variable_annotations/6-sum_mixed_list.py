#!/usr/bin/env python3
"""Sum of list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum of list"""
    return sum(num for num in mxd_lst)
