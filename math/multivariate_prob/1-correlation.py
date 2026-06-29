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
    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError(c_ver)

    std = np.sqrt(np.diag(C))

    return C / std[:, None] / std[None, :]
