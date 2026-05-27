#!/usr/bin/env python3
"""Module spits definiteness of matrix"""
import numpy as np


def definiteness(matrix):
    """Validate matrix"""
    mtx = matrix
    if not isinstance(mtx, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    n = len(mtx)
    if len(mtx.shape) != 2 or mtx.shape[0] != mtx.shape[1]:
        return None
    if not np.allclose(mtx, mtx.T):
        return None

    """Calc array of determinants with np.slicing"""
    mtx_dets = np.array([np.linalg.det(mtx[:i, :i]) for i in range(1, n + 1)])

    """Figure definiteness"""
    if np.all(mtx_dets > 0):
        return "Positive definite"
    elif np.all(mtx_dets >= 0) and np.any(mtx_dets == 0):
        return "Positive semi-definite"
    elif np.all(mtx_dets < 0):
        return "Negative definite"
    elif np.all(mtx_dets <= 0) and np.any(mtx_dets == 0):
        return "Negative semi-definite"
    elif np.any(mtx_dets < 0) and np.any(mtx_dets > 0):
        return "Indefinite"
    else:
        return None
