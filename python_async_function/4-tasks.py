#!/usr/bin/env python3
"""Basic async"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Basic async"""
    wait_list = []
    for _ in range(n):
        wait_list.append(await task_wait_random(max_delay))
    return sorted(wait_list)
