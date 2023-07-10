#!/usr/bin/env python3
"""
wait_n: async routine that takes in 2 int arguments (in this order):
n and max_delay. spawn wait_random n times with the specified max_delay
return the list of all the delays (float values). The list of the delays
should be in ascending order without using sort() because of concurrency.
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays (float values) sorted in
    ascending order without using sort()
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    # sorted_list = []
    # while delays:
    #     min_Num = delays[0]
    #     for i in delays:
    #         if i < min_Num:
    #             min_Num = i
    #     sorted_list.append(min_Num)
    #     delays.remove(min_Num)
    return sorted(delays)
