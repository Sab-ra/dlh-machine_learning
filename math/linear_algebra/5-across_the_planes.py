#!/usr/bin/env python3
"""Add two matrices"""

def add_matrices2D(mat1, mat2):
    """Element-wize"""
    matrix = []
    msh = __import__('2-size_me_please')
    if mat1 == [] and mat2 == []:
        return []
    if mat1 == [] or mat2 == []:
        return None
    if msh.matrix_shape(mat1) != msh.matrix_shape(mat2):
        return None
    else:
        matrix = []
        for row1, row2 in zip(mat1, mat2):
            matrix.append([x + y for x, y in zip(row1, row2)])
        return matrix
