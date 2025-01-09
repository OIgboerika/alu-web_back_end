#!/usr/bin/env python3
"""Contains typed function element_length"""
from typing import Iterable, Tuple, List


def element_length(lst: Iterable[str]) -> List[Tuple[str, int]]:
    """Returns list of tuples containing string and its length"""
    return [(i, len(i)) for i in lst]
