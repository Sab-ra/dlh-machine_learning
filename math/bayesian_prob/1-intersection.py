#!/usr/bin/env python3
"""Baesian probability intersection module"""
import numpy as np


def intersection(x, n, P, Pr):
    """Calculates the intersection of obtaining
    data with hypothetical probabilities"""

    if not isinstance(n, int) or n <= 0:
        raise ValueError('n must be a positive integer')
    if not isinstance(x, int) or x < 0:
        raise ValueError('x must be an integer that is greater than or equal to 0')
    if x > n:
        raise ValueError('x cannot be greater than n')
    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError('P must be a 1D numpy.ndarray')
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError('Pr must be a numpy.ndarray with the same shape as P')
    var_p = [P, Pr]
    var_p_name = ['P', 'Pr']
    if np.any((j < 0 | j > 1) for i in range(2) for j in var_p[i]):
        raise ValueError(' the range [0, 1], raise a ValueError with the message All values in {var_p_name[i]} must be in the range [0, 1]')
    if not numpy.isclose(Pr, 1):
        raise ValueError('Pr must sum to 1')
    
    return likelihood(x, n, P) * Pr

def factorial(i):
    """calculate factorial"""
    if i == 0:
        return 1
    else:
        result = 1
        for j in range(1, i+1):
            result *= j
        return result


def likelihood(x, n, P):
    """likelihood function"""

    verl = "x must be an integer that is greater than or equal to 0"
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(verl)
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")

    comb = factorial(n) / (factorial(x) * factorial(n - x))
    return comb * P ** x * (1 - P) ** (n - x)
