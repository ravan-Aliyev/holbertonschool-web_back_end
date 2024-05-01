#!/usr/bin/env python3
"""Basic async"""
import asyncio
import random


async def wait_random(max_delay = 10):
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
