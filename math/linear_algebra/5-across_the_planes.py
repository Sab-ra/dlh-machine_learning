#!/usr/bin/env python3
"""Add two matrices"""


def add_matrices2D(mat1, mat2):
    """Element-wize"""

    if len(mat1) != len(mat2):
        return None
    if len(mat1[0]) != len(mat2[0]):
        return None

    matrix = []
    for row1, row2 in zip(mat1, mat2):
        matrix.append([x + y for x, y in zip(row1, row2)])
    return matrix
