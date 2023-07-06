#!/usr/bin/env python3
"""
Annotate the function’s parameters and return values with appropriate types
"""

from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns iterable"""
    return [(i, len(i)) for i in lst]
