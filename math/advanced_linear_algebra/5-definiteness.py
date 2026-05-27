#!/usr/bin/env python3
"""Module spits definiteness of matrix"""
import numpy as np


def definiteness(matrix):
    """Validate matrix"""
    mtx = matrix
    if not isinstance(mtx, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    n = len(mtx)
    if not all(len(mtx[row]) == n for row in mtx):
        return None
    if not np.allclose(mtx, mtx.T):
        return None

    """Calc array of determinants"""
    mtx_dets = []
    for i in range(1, (n + 1)):
        shmatrix = []
        for row in range(i):
            shmatrix_row = []
            for col in range(i):
                shmatrix_row.append(mtx[row][col])
            shmatrix.append(shmatrix_row)
        mtx_dets.append(np.linalg.det(shmatrix))
    
    mtx_dets = np.array(mtx_dets)

    """Figure definiteness"""
    if np.all(mtx_dets > 0):
        return "Positive definite"
    elif np.all(mtx_dets >= 0) and np.any(mtx_dets == 0):
        return "Positive semi-definite"
    elif np.all(mtx_dets < 0):
        return "Negative definite"
    elif np.all(mtx_dets <= 0) and np.any(mtx_dets == 0):
        return "Netative semi-definite"
    elif np.any(mtx_dets < 0) and np.any(mtx_dets > 0):
        return "Indefinite"
    else:
        return None
