#!/usr/bin/env python3
"""Module recursive sum of i**2"""


def summation_i_squared(n):
    """Function will rock integers from 1 to n"""
    if not isinstance(n, int) or n < 1:
        print('Piss off')
        return None
    else:
        list_of_numbers = [x for x in range(1, n + 1)]
        if len(list_of_numbers) == 1:
            return 1
        return list_of_numbers[-1] ** 2 + summation_i_squared(n-1)
