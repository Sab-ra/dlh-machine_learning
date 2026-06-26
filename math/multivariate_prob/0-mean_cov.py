#!/usr/bin/env python3
"""Mean and Covariance"""
import numpy as np


def mean_cov(X):
    """Squash Mean and Covariance out of X"""

    # Error messages
    x_ter = f'X must be a 2D numpy.ndarray'
    x_ver = f'X must contain multiple data points'

    if not isinstance(X, np.ndarray) or len(X.shape) !=2:
        raise TypeError(x_ter)
    # n = number of trials, d = number of dimensions (rank, die, etc.)
    n, d = X.shape
    if n < 2:
        raise ValueError(x_ver)
    
    # 1. Calculate the Mean Vector (mu)
    # We take the average of each column. 
    # keepdims=True ensures the shape is (1, d) instead of just (d,)
    mean = np.mean(X, axis=0, keepdims=True)

    # 2. Calculate the Covariance Matrix (Sigma)
    # First, center the data by subtracting the mean from every trial
    X_centered = X - mean

    # Then, perform the "Product of Differences" for all dimensions at once.
    # Matrix multiplication (@) of (X-mu).T and (X-mu) handles the 
    # (Rank - mu_rank) * (Die - mu_die) math for every pair.
    # We divide by n to get the average, as used in your manual 5-trial example.
    cov = (X_centered.T @ X_centered) / n

    return mean, cov
    