#!/usr/bin/env python3
"""Compute Correlation matrix out of
given Covariance matrix"""
import numpy as np


def correlation(C):
    """using broadcasting"""

    # Error messages
    c_ter = f'C must be a numpy.ndarray'
    c_ver = f'C must be a 2D square matrix'

    if not isinstance(C, np.ndarray):
        raise TypeError(c_ter)
    n, d = C.shape
    if n != d or C.ndim != 2:
        raise ValueError(c_ver)
    pass