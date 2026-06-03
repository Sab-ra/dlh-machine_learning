#!/usr/bin/env python3
"""Module recursive sum of i**2"""


def summation_i_squared(n):
    """Function will rock integers from 1 to n"""
    if not isinstance(n, int) or n < 1:
        return None
    else:
        return (n * (n + 1) * (2 * n + 1)) / 6
