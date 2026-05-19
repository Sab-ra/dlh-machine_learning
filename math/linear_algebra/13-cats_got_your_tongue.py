#!/usr/bin/env python3
"""Concatenate along axis"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """document"""
    return np.concatenate((mat1, mat2), axis=axis)
