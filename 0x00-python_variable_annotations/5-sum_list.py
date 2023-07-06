#!/usr/bin/env python3
"""
sum_list: type-annotated function  which takes a list input_list of
floats as argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns sum of all elements in the list
        Args:
            input_list: List of floats
    """
    total: float = 0.0
    for i in range(len(input_list)):
        total += input_list[i]
    return total
