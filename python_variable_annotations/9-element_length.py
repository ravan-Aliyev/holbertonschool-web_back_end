#!/usr/bin/env python3
"""Kv of list"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Element list"""
    return [(i, len(i)) for i in lst]
