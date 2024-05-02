#!/usr/bin/env python3
"""Async Generator"""
import asyncio
from typing import Generator
from random import random


async def async_generator() -> Generator[float, None, None]:
    """Async generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random() * 10
