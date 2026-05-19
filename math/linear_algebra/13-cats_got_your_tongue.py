#!/usr/bin/env python3
"""Concatenate matrices"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Call with numpy imported"""
    return np.concatenate((mat1, mat2), axis=axis)
