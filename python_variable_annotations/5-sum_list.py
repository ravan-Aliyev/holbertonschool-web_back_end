#!/usr/bin/env python3
"""Sum of list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum of list"""
    return sum(num for num in input_list)
