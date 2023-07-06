#!/usr/bin/env python3
"""
sum_mixed_list: type-annotated function that takes a list mxd_lst of integers
and floats and returns their sum as a float.
"""


from typing import List, Union, Optional


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of elements of mixed list as float"""
    total: float = 0.0
    for i in range(len(mxd_lst)):
        total += mxd_lst[i]
    return total
