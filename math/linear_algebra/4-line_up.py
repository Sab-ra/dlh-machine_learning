#!/usr/bin/env python3
"""Module to sum arrays"""


def add_arrays(arr1, arr2):
    """Element-wise addition"""
    result = []
    if len(arr1) != len(arr2):
        return None
    else:
        result = [x + y for x, y in zip(arr1, arr2)]
    return result