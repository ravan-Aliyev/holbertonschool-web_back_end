#!/usr/bin/env python3
"""Kv of list"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Kv of list"""
    def real_multiplier(num: float) -> float:
        """Multiplier"""
        return num * multiplier

    return real_multiplier
