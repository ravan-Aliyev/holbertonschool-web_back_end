#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Async comprehensions"""
    s = time.time()
    async_list = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*async_list)
    elased = time.time()
    return elased - s