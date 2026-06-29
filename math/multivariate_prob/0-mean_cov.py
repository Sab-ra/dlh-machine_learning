#!/usr/bin/env python3
"""Compute mean vector and covariance matrix for a dataset."""
import numpy as np


def mean_cov(X):
    """Squash Mean and Covariance out of X"""

    # Error messages
    x_ter = f'X must be a 2D numpy.ndarray'
    x_ver = f'X must contain multiple data points'

    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError(x_ter)
    # n = number of rows, _ (d) = number columns (shape of matrix like 4*2)
    n, _ = X.shape
    if n < 2:
        raise ValueError(x_ver)

    mean = np.mean(X, axis=0, keepdims=True)
    X_centered = X - mean

    cov = (X_centered.T @ X_centered) / (n - 1)

    return mean, cov
