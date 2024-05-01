#!/usr/bin/env python3
"""Basic async"""
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    wait_list = []
    for _ in range(n):
        wait_list.append(await wait_random(max_delay))
    return sorted(wait_list)
