#!/usr/bin/env python3
"""
make_multiplier: type-annotated function that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier
"""

from typing import Callable, Union, Optional


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a a function that multiplies a float by multiplier"""
    return lambda x: x * multiplier
