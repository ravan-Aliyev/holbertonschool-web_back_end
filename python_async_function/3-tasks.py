#!/usr/bin/env python3
"""Basic async"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """Basic async"""
    return asyncio.Task(wait_random(max_delay))
