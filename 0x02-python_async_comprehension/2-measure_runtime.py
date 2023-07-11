#!/usr/bin/env python3
"""
measure_runtime: The coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
It should measure the total runtime and return it.
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return total run time"""
    start = time.perf_counter()
    # Schedule 4 calls concurrently
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
