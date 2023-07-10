#!/usr/bin/env python3
"""
task_wait_n: async coroutine that alter `wait_n` into a new function.
The code is nearly identical except task_wait_random is being called
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays (float values) sorted in
    ascending order without using sort()
    """
    delays = [await task_wait_random(max_delay) for _ in range(n)]
    sorted_list = []
    while delays:
        min_Num = delays[0]
        for i in delays:
            if i < min_Num:
                min_Num = i
        sorted_list.append(min_Num)
        delays.remove(min_Num)
    return sorted_list
