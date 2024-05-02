#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
from typing import Generator, List
from random import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async comprehensions"""
    result = []
    async for i in async_generator():
        result.append(i)
    return result
