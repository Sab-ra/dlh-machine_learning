#!/usr/bin/env python3
"""Bayesian probability Posterior module"""
import numpy as np


def posterior(x, n, P, Pr):
    """Posterior P(H|E) is an adjusted upon new evidance belief
    P(H|E) = P(E|H) * P(H)  /  P(E)
    """

    #Error messages
    n_ver = f'n must be a positive integer'
    x_ver = f'x must be an integer that is greater than or equal to 0'
    x_ver_n = f'x cannot be greater than n'
    p_ter = f'P must be a 1D numpy.ndarray'
    pr_ter = f'Pr must be a numpy.ndarray with the same shape as P'
    pr_ver_1 = f'Pr must sum to 1'

    if not isinstance(n, int) or n <= 0:
        raise ValueError(n_ver)
    if not isinstance(x, int) or x < 0:
        raise ValueError(x_ver)
    if x > n:
        raise ValueError(x_ver_n)
    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError(p_ter)
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError(pr_ter)
    var_p = [P, Pr]
    for i in range(2):
        name_domain = ['P', 'Pr']
        var_p_name = name_domain[i]
        j = var_p[i]
        p_pr_ver = f'All values in {var_p_name} must be in the range [0, 1]'
        if np.any((j < 0) | (j > 1)):
            raise ValueError(p_pr_ver)
    if not np.isclose(sum(Pr), 1):
        raise ValueError(pr_ver_1)
    
    return intersection(x, n, P, Pr) / marginal(x, n, P, Pr)


def marginal(x, n, P, Pr):
    """P(E)"""

    return np.sum(intersection(x, n, P, Pr))


def intersection(x, n, P, Pr):
    """P(E|H)*P(E)"""

    return likelihood(x, n, P) * Pr


def likelihood(x, n, P):
    """P(E|H)"""

    return comb(x, n) * P ** x * (1 - P) ** (n - x)


def comb(x, n):
    """number of possible combinations
    of desired quantity of win: x in n trails"""

    return factorial(n) / (factorial(x) * factorial(n - x))


def factorial(natural_number):
    """natural_number!"""

    if natural_number == 0:
        return 1
    else:
        result = 1
        for i in range(natural_number + 1):
            result *= i
        return round(result)
