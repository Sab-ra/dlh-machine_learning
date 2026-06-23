#!/usr/bin/env python3
"""Bayesian probability marginal module"""
import numpy as np


def marginal(x, n, P, Pr):
    """Bayesian formula denominator
    calculates a sum of all intersections"""

    # Error messages for Likelihood:
    n_ver = f'n must be a positive integer'
    x_ver = f'x must be an integer that is greater than or equal to 0'
    x_ver_n = f'x cannot be greater than n'
    p_ter = f'P must be a 1D numpy.ndarray'
    pr_ter = f'Pr must be a numpy.ndarray with the same shape as P'
    p_ver = f'All values in P must be in the range [0, 1]'
    pr_ver = f'All values in Pr must be in the range [0, 1]'
    pr_ver_1 = f'Pr must sum to 1'

    if not isinstance(n, int) or n < 0:
        raise ValueError(n_ver)
    if not isinstance(x, int) or x < 0:
        raise ValueError(x_ver)
    if x > n:
        raise ValueError(x_ver_n)
    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError(p_ter)
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError(pr_ter)
    if np.any(P < 0 | P > 1):
        raise ValueError(p_ver)
    if np.any(Pr < 0 | Pr > 1):
        raise ValueError(pr_ver)
    if not np.isclose(sum(Pr), 1):
        raise ValueError(pr_ver_1)

    return np.sum(intersection(x, n, P, Pr))

def intersection(x, n, P, Pr):
    """Intersection is a
    product of likelihood and initial belief"""

    return likelihood(x, n, P) * Pr


def likelihood(x, n, P):
    """likelihood is a
    probability of evidence showing up
    given that hypothesis is true"""

    # lklhd = comb(n,x) * p^x * (1-p)^(n-x)
    comb = factorial(n) / (factorial(x) - factorial(n - x))
    return comb * P ** x * (1 - P) ** (n - x)


def factorial(natural_number):
    """calculate factorial
    of a natural_number!"""
    # Error messages:
    ter = 'factorial may be taken only of natural number'

    try:
        if natural_number == 0:
            return 1
        else:
            result = 1
            for j in range(1, natural_number+1):
                result *= j
            return result
    except TypeError:
        print(ter)
