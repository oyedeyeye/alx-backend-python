#!/usr/bin/env python3
"""
wait_random: Asynchronous coroutine that takes in integer argument (max_delay)
waits for a random delay between 0 and max_delay (included and float value)
seconds and eventually returns it.
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that Returns a float"""
    i: float = random.random() * max_delay
    await asyncio.sleep(i)
    return i
