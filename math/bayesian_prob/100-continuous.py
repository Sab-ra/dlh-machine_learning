#!/usr/bin/env python3
"""
Bayesian Posterior based on given range
"""
from scipy import special


def posterior(x, n, p1, p2):
    """
    Posterior that p is within the range
    """

    # Error messages
    n_ver = f'n must be a positive integer'
    x_ver = f'x must be an integer that is greater than or equal to 0'
    x_ver_n = f'x cannot be greater than n'
    # p_ver = f'{p} must be a float in the range [0, 1]' - in loop
    r_ver = f'p2 must be greater than p1'

    if not isinstance(n, int) or n <= 0:
        raise ValueError(n_ver)
    if not isinstance(x, int) or x < 0:
        raise ValueError(x_ver)
    if x > n:
        raise ValueError(x_ver_n)
    var_p = [p1, p2]
    name_domain = ['p1', 'p2']
    for i in range(2):
        j = var_p[i]
        var_p_name = name_domain[i]
        p_ver = f'{var_p_name} must be a float in the range [0, 1]'
        if not isinstance(j, float) or not 0 <= j <= 1:
            raise ValueError(p_ver)
    if p2 <= p1:
        raise ValueError(r_ver)

    prob_1 = cdf(x, n, p1)
    prob_2 = cdf(x, n, p2)
    return float(prob_2 - prob_1)


def cdf(x, n, p):
    """Probability Beta CDF
    special.betainc is the regularized incomplete beta function
    """

    a, b = data(x, n)
    return special.betainc(a, b, p)


def data(x, n):
    """Beta distribution parameters"""

    a = x + 1
    b = (n - x) + 1
    return a, b
