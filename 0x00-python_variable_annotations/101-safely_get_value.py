#!/usr/bin/env python3
"""
Given the parameters and return values, add type annotations to the function
Hint: look into TypeVar
"""


from typing import Union, TypeVar, Mapping, Any


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """Returns typeVar or any type"""
    if key in dct:
        return dct[key]
    else:
        return default
