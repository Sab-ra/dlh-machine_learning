#!/usr/bin/env python3
"""Concatenate matrices"""


def np_cat(mat1, mat2, axis=0):
    """Call with numpy imported"""
    return np.concatenate((mat1, mat2), axis=0)
