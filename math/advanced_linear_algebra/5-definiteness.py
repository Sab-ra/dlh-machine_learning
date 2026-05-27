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

    try:
        # Eigenvalues tell the whole story
        vals = np.linalg.eigvals(mtx)
    except np.linalg.LinAlgError:
        return None

    # Check conditions element-wise
    if np.all(vals > 0):
        return "Positive definite"
    if np.all(vals >= 0) and np.any(np.isclose(vals, 0)):
        return "Positive semi-definite"
    if np.all(vals < 0):
        return "Negative definite"
    if np.all(vals <= 0) and np.any(np.isclose(vals, 0)):
        return "Negative semi-definite"
    if np.any(vals > 0) and np.any(vals < 0):
        return "Indefinite"

    return None
